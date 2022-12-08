# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Currently the documentation for 200 responses to Block create, read, update, and delete (CRUD) operations is incorrect. This is due to an issue with our documentation generator.  Under each Block Group, the documentation will show `name`, `collection`, and `data` keys.  In reality, this level does not exist and should be skipped.  See the schema under the `data` key of a Template's Block Group for the correct schema of such Block Group. - Error responses are most specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 3.3.1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from sedaro_base_client import schemas  # noqa: F401


class ConstantLoad(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "loadDefParams",
            "loadState",
            "loadDefType",
            "name",
            "epsOutputType",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class epsOutputType(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            EpsOutputTypes,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'epsOutputType':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            loadState = schemas.StrSchema
            
            
            class loadDefType(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            ConstantLoadDefinitionTypes,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'loadDefType':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class loadDefParams(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            ConstantPower,
                            ConstantResistance,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'loadDefParams':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            id = schemas.StrSchema
            busRegulator = schemas.StrSchema
            topology = schemas.StrSchema
            powerConsumed = schemas.NumberSchema
            isActive = schemas.BoolSchema
            dutyCyclePeriod = schemas.NumberSchema
            
            
            class dutyCyclePercentage(
                schemas.NumberSchema
            ):
                pass
            __annotations__ = {
                "name": name,
                "epsOutputType": epsOutputType,
                "loadState": loadState,
                "loadDefType": loadDefType,
                "loadDefParams": loadDefParams,
                "id": id,
                "busRegulator": busRegulator,
                "topology": topology,
                "powerConsumed": powerConsumed,
                "isActive": isActive,
                "dutyCyclePeriod": dutyCyclePeriod,
                "dutyCyclePercentage": dutyCyclePercentage,
            }
    
    loadDefParams: MetaOapg.properties.loadDefParams
    loadState: MetaOapg.properties.loadState
    loadDefType: MetaOapg.properties.loadDefType
    name: MetaOapg.properties.name
    epsOutputType: MetaOapg.properties.epsOutputType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["epsOutputType"]) -> MetaOapg.properties.epsOutputType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loadState"]) -> MetaOapg.properties.loadState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loadDefType"]) -> MetaOapg.properties.loadDefType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loadDefParams"]) -> MetaOapg.properties.loadDefParams: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["busRegulator"]) -> MetaOapg.properties.busRegulator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topology"]) -> MetaOapg.properties.topology: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["powerConsumed"]) -> MetaOapg.properties.powerConsumed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isActive"]) -> MetaOapg.properties.isActive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dutyCyclePeriod"]) -> MetaOapg.properties.dutyCyclePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dutyCyclePercentage"]) -> MetaOapg.properties.dutyCyclePercentage: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "epsOutputType", "loadState", "loadDefType", "loadDefParams", "id", "busRegulator", "topology", "powerConsumed", "isActive", "dutyCyclePeriod", "dutyCyclePercentage", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["epsOutputType"]) -> MetaOapg.properties.epsOutputType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loadState"]) -> MetaOapg.properties.loadState: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loadDefType"]) -> MetaOapg.properties.loadDefType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loadDefParams"]) -> MetaOapg.properties.loadDefParams: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["busRegulator"]) -> typing.Union[MetaOapg.properties.busRegulator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topology"]) -> typing.Union[MetaOapg.properties.topology, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["powerConsumed"]) -> typing.Union[MetaOapg.properties.powerConsumed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isActive"]) -> typing.Union[MetaOapg.properties.isActive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dutyCyclePeriod"]) -> typing.Union[MetaOapg.properties.dutyCyclePeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dutyCyclePercentage"]) -> typing.Union[MetaOapg.properties.dutyCyclePercentage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "epsOutputType", "loadState", "loadDefType", "loadDefParams", "id", "busRegulator", "topology", "powerConsumed", "isActive", "dutyCyclePeriod", "dutyCyclePercentage", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        loadDefParams: typing.Union[MetaOapg.properties.loadDefParams, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        loadState: typing.Union[MetaOapg.properties.loadState, str, ],
        loadDefType: typing.Union[MetaOapg.properties.loadDefType, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        epsOutputType: typing.Union[MetaOapg.properties.epsOutputType, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        busRegulator: typing.Union[MetaOapg.properties.busRegulator, str, schemas.Unset] = schemas.unset,
        topology: typing.Union[MetaOapg.properties.topology, str, schemas.Unset] = schemas.unset,
        powerConsumed: typing.Union[MetaOapg.properties.powerConsumed, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        isActive: typing.Union[MetaOapg.properties.isActive, bool, schemas.Unset] = schemas.unset,
        dutyCyclePeriod: typing.Union[MetaOapg.properties.dutyCyclePeriod, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        dutyCyclePercentage: typing.Union[MetaOapg.properties.dutyCyclePercentage, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConstantLoad':
        return super().__new__(
            cls,
            *_args,
            loadDefParams=loadDefParams,
            loadState=loadState,
            loadDefType=loadDefType,
            name=name,
            epsOutputType=epsOutputType,
            id=id,
            busRegulator=busRegulator,
            topology=topology,
            powerConsumed=powerConsumed,
            isActive=isActive,
            dutyCyclePeriod=dutyCyclePeriod,
            dutyCyclePercentage=dutyCyclePercentage,
            _configuration=_configuration,
            **kwargs,
        )

from sedaro_base_client.model.constant_load_definition_types import ConstantLoadDefinitionTypes
from sedaro_base_client.model.constant_power import ConstantPower
from sedaro_base_client.model.constant_resistance import ConstantResistance
from sedaro_base_client.model.eps_output_types import EpsOutputTypes