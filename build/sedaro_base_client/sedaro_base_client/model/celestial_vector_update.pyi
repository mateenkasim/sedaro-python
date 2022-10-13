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


class CelestialVectorUpdate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "vectorType",
            "name",
            "celestialPointingDirection",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class vectorType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CELESTIAL(cls):
                    return cls("CELESTIAL")
        
            @staticmethod
            def celestialPointingDirection() -> typing.Type['CelestialPointingDirections']:
                return CelestialPointingDirections
            id = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "vectorType": vectorType,
                "celestialPointingDirection": celestialPointingDirection,
                "id": id,
            }
    
    vectorType: MetaOapg.properties.vectorType
    name: MetaOapg.properties.name
    celestialPointingDirection: 'CelestialPointingDirections'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vectorType"]) -> MetaOapg.properties.vectorType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["celestialPointingDirection"]) -> 'CelestialPointingDirections': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "vectorType", "celestialPointingDirection", "id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vectorType"]) -> MetaOapg.properties.vectorType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["celestialPointingDirection"]) -> 'CelestialPointingDirections': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "vectorType", "celestialPointingDirection", "id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        vectorType: typing.Union[MetaOapg.properties.vectorType, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        celestialPointingDirection: 'CelestialPointingDirections',
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CelestialVectorUpdate':
        return super().__new__(
            cls,
            *args,
            vectorType=vectorType,
            name=name,
            celestialPointingDirection=celestialPointingDirection,
            id=id,
            _configuration=_configuration,
            **kwargs,
        )

from sedaro_base_client.model.celestial_pointing_directions import CelestialPointingDirections
