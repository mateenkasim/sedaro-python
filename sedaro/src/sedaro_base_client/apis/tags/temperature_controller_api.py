# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).   # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""

from sedaro_base_client.paths.models_branches_branch_id_thermal_temp_controllers_coolers_.post import CreateCooler
from sedaro_base_client.paths.models_branches_branch_id_thermal_temp_controllers_heaters_.post import CreateHeater
from sedaro_base_client.paths.models_branches_branch_id_thermal_temp_controllers_coolers_block_id.delete import DeleteCooler
from sedaro_base_client.paths.models_branches_branch_id_thermal_temp_controllers_heaters_block_id.delete import DeleteHeater
from sedaro_base_client.paths.models_branches_branch_id_thermal_temp_controllers_coolers_block_id.patch import UpdateCooler
from sedaro_base_client.paths.models_branches_branch_id_thermal_temp_controllers_heaters_block_id.patch import UpdateHeater


class TemperatureControllerApi(
    CreateCooler,
    CreateHeater,
    DeleteCooler,
    DeleteHeater,
    UpdateCooler,
    UpdateHeater,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass