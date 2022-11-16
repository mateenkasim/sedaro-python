# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com   # noqa: E501

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


class SatelliteUpdate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            mass = schemas.NumberSchema
            inertia = schemas.AnyTypeSchema
            earthshineIrradiance = schemas.NumberSchema
            
            
            class albedo(
                schemas.NumberSchema
            ):
                pass
            
            
            class dragTorque(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dragTorque':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class gravityGradientTorque(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'gravityGradientTorque':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "mass": mass,
                "inertia": inertia,
                "earthshineIrradiance": earthshineIrradiance,
                "albedo": albedo,
                "dragTorque": dragTorque,
                "gravityGradientTorque": gravityGradientTorque,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mass"]) -> MetaOapg.properties.mass: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inertia"]) -> MetaOapg.properties.inertia: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["earthshineIrradiance"]) -> MetaOapg.properties.earthshineIrradiance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["albedo"]) -> MetaOapg.properties.albedo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dragTorque"]) -> MetaOapg.properties.dragTorque: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gravityGradientTorque"]) -> MetaOapg.properties.gravityGradientTorque: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "mass", "inertia", "earthshineIrradiance", "albedo", "dragTorque", "gravityGradientTorque", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mass"]) -> typing.Union[MetaOapg.properties.mass, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inertia"]) -> typing.Union[MetaOapg.properties.inertia, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["earthshineIrradiance"]) -> typing.Union[MetaOapg.properties.earthshineIrradiance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["albedo"]) -> typing.Union[MetaOapg.properties.albedo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dragTorque"]) -> typing.Union[MetaOapg.properties.dragTorque, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gravityGradientTorque"]) -> typing.Union[MetaOapg.properties.gravityGradientTorque, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "mass", "inertia", "earthshineIrradiance", "albedo", "dragTorque", "gravityGradientTorque", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        mass: typing.Union[MetaOapg.properties.mass, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        inertia: typing.Union[MetaOapg.properties.inertia, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        earthshineIrradiance: typing.Union[MetaOapg.properties.earthshineIrradiance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        albedo: typing.Union[MetaOapg.properties.albedo, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        dragTorque: typing.Union[MetaOapg.properties.dragTorque, list, tuple, schemas.Unset] = schemas.unset,
        gravityGradientTorque: typing.Union[MetaOapg.properties.gravityGradientTorque, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SatelliteUpdate':
        return super().__new__(
            cls,
            *args,
            id=id,
            mass=mass,
            inertia=inertia,
            earthshineIrradiance=earthshineIrradiance,
            albedo=albedo,
            dragTorque=dragTorque,
            gravityGradientTorque=gravityGradientTorque,
            _configuration=_configuration,
            **kwargs,
        )
