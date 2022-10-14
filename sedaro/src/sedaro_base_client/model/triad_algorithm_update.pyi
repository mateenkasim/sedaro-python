# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).   # noqa: E501

    The version of the OpenAPI document: 3.0.0
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


class TriadAlgorithmUpdate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "algorithmType",
            "rate",
            "name",
            "algorithmSubtype",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            rate = schemas.NumberSchema
            
            
            class algorithmType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ATTITUDE_DETERMINATION(cls):
                    return cls("ATTITUDE_DETERMINATION")
        
            @staticmethod
            def algorithmSubtype() -> typing.Type['AttDetTypes']:
                return AttDetTypes
            id = schemas.StrSchema
            
            
            class attitudeSolution(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'attitudeSolution':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class angularVelocitySolution(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'angularVelocitySolution':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "rate": rate,
                "algorithmType": algorithmType,
                "algorithmSubtype": algorithmSubtype,
                "id": id,
                "attitudeSolution": attitudeSolution,
                "angularVelocitySolution": angularVelocitySolution,
            }
    
    algorithmType: MetaOapg.properties.algorithmType
    rate: MetaOapg.properties.rate
    name: MetaOapg.properties.name
    algorithmSubtype: 'AttDetTypes'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rate"]) -> MetaOapg.properties.rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["algorithmType"]) -> MetaOapg.properties.algorithmType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["algorithmSubtype"]) -> 'AttDetTypes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attitudeSolution"]) -> MetaOapg.properties.attitudeSolution: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["angularVelocitySolution"]) -> MetaOapg.properties.angularVelocitySolution: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "rate", "algorithmType", "algorithmSubtype", "id", "attitudeSolution", "angularVelocitySolution", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rate"]) -> MetaOapg.properties.rate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["algorithmType"]) -> MetaOapg.properties.algorithmType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["algorithmSubtype"]) -> 'AttDetTypes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attitudeSolution"]) -> typing.Union[MetaOapg.properties.attitudeSolution, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["angularVelocitySolution"]) -> typing.Union[MetaOapg.properties.angularVelocitySolution, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "rate", "algorithmType", "algorithmSubtype", "id", "attitudeSolution", "angularVelocitySolution", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        algorithmType: typing.Union[MetaOapg.properties.algorithmType, str, ],
        rate: typing.Union[MetaOapg.properties.rate, decimal.Decimal, int, float, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        algorithmSubtype: 'AttDetTypes',
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        attitudeSolution: typing.Union[MetaOapg.properties.attitudeSolution, list, tuple, schemas.Unset] = schemas.unset,
        angularVelocitySolution: typing.Union[MetaOapg.properties.angularVelocitySolution, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TriadAlgorithmUpdate':
        return super().__new__(
            cls,
            *args,
            algorithmType=algorithmType,
            rate=rate,
            name=name,
            algorithmSubtype=algorithmSubtype,
            id=id,
            attitudeSolution=attitudeSolution,
            angularVelocitySolution=angularVelocitySolution,
            _configuration=_configuration,
            **kwargs,
        )

from sedaro_base_client.model.att_det_types import AttDetTypes
