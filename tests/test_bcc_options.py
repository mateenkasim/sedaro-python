from config import API_KEY, HOST, WILDFIRE_A_T_ID, WILDFIRE_SCENARIO_ID

from sedaro import SedaroApiClient
from sedaro.block_class_client import BlockClassClient
from sedaro.block_client import BlockClient


def test_block_class_client_options():
    agent_template_blocks = [
        'AngularVelocitySensor',
        'AveragingAlgorithm',
        'Battery',
        'BatteryCell',
        'BatteryPack',
        'BodyFrameVector',
        'BusRegulator',
        'CelestialTarget',
        'CelestialVector',
        'CircularFieldOfView',
        'Component',
        'Condition',
        'ConOps',  # no associated API, added this one manually
        'ConstantLoad',
        'Cooler',
        'DirectionSensor',
        'EKFAlgorithm',
        'FOVConstraint',
        'FuelReservoir',
        'GPSAlgorithm',
        'GroundTarget',
        'GroupCondition',
        'Heater',
        'LoadState',
        'LocalVector',
        'LockPointingMode',
        'Magnetorquer',
        'MaxAlignPointingMode',
        'MEKFAlgorithm',
        'OperationalMode',
        'OpticalAttitudeSensor',
        'PassivePointingMode',
        'PIDAlgorithm',
        'PositionSensor',
        'ReactionWheel',
        'RectangularFieldOfView',
        'Satellite',
        'SlidingModeAlgorithm',
        'SolarArray',
        'SolarCell',
        'SolarPanel',
        'SpaceTarget',
        'SphericalFuelTank',
        'SpherocylinderFuelTank',
        'StaticThrustControlAlgorithm',
        'Subsystem',
        'Surface',
        'SurfaceMaterial',
        'TargetGroup',
        'TargetGroupVector',
        'TargetVector',
        'TempControllerState',
        'ThermalInterface',
        'ThermalInterfaceMaterial',
        'Thruster',
        'PowerProcessor',
        'TriadAlgorithm',
        'VectorSensor',
    ]
    scenario_blocks = [
        'Agent',
        'ClockConfig',
        'Orbit',
    ]
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        for branch_id, blocks in [[WILDFIRE_A_T_ID, agent_template_blocks], [WILDFIRE_SCENARIO_ID, scenario_blocks]]:
            branch_client = sedaro_client.get_branch(branch_id)

            for block in blocks:
                bcc = getattr(branch_client, block)
                assert isinstance(bcc, BlockClassClient)

                # CHECK: these blocks can't be "created"
                if any(string in block for string in ['PowerProcessor', 'Satellite', 'ConOps']) or block == 'Battery':
                    try:
                        getattr(bcc, 'create')()
                    except AttributeError as e:
                        err_msg = str(e)
                        assert err_msg == f'There is no create method on a "{block}" BlockClassClient because this type of Sedaro Block is not createable.'
                    continue

                # TODO: temp_crud
                # CHECK: for all others, make sure create() exists, can be called, and raises error when called empty
                # try:
                #     getattr(bcc, 'create')()
                # except TypeError as e:
                #     assert (all(
                #         s in str(e) for s in {'__new__() missing', 'required keyword-only argument'}
                #     ) or str(e) == 'No input given. args or kwargs must be given.')
                # except Exception as e:
                #     # print any other erros that happen
                #     print(block, type(e), str(e))

                # CHECK: can use get_all method
                all_blocks_of_type = getattr(bcc, 'get_all')()
                assert type(all_blocks_of_type) == list
                if len(all_blocks_of_type):
                    assert isinstance(all_blocks_of_type[0], BlockClient)

        for bad_block in ['try_me', 'and_me', 'NO_wayYou_will_CatchMe!!!!!!']:
            try:
                bcc = getattr(branch_client, bad_block)
            except AttributeError as e:
                expected_err = f'Unable to create a "BlockClassClient" from string: "{bad_block}". Please check the name and try again.'
                assert str(e) == expected_err


def run_tests():
    test_block_class_client_options()
