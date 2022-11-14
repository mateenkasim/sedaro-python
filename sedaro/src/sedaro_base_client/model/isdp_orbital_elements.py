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


class ISDPOrbitalElements(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "a",
            "e",
            "nu",
            "raan",
            "om",
            "inc",
        }
        
        class properties:
            
            
            class a(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 6478.1359999999995
            
            
            class e(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            
            
            class inc(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 180.0
                    inclusive_minimum = 0.0
            
            
            class raan(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 360.0
                    inclusive_minimum = 0.0
            
            
            class om(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 360.0
                    inclusive_minimum = 0.0
            
            
            class nu(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 360.0
                    inclusive_minimum = 0.0
            __annotations__ = {
                "a": a,
                "e": e,
                "inc": inc,
                "raan": raan,
                "om": om,
                "nu": nu,
            }
    
    a: MetaOapg.properties.a
    e: MetaOapg.properties.e
    nu: MetaOapg.properties.nu
    raan: MetaOapg.properties.raan
    om: MetaOapg.properties.om
    inc: MetaOapg.properties.inc
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["a"]) -> MetaOapg.properties.a: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["e"]) -> MetaOapg.properties.e: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inc"]) -> MetaOapg.properties.inc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["raan"]) -> MetaOapg.properties.raan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["om"]) -> MetaOapg.properties.om: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nu"]) -> MetaOapg.properties.nu: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["a", "e", "inc", "raan", "om", "nu", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["a"]) -> MetaOapg.properties.a: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["e"]) -> MetaOapg.properties.e: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inc"]) -> MetaOapg.properties.inc: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["raan"]) -> MetaOapg.properties.raan: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["om"]) -> MetaOapg.properties.om: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nu"]) -> MetaOapg.properties.nu: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["a", "e", "inc", "raan", "om", "nu", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        a: typing.Union[MetaOapg.properties.a, decimal.Decimal, int, float, ],
        e: typing.Union[MetaOapg.properties.e, decimal.Decimal, int, float, ],
        nu: typing.Union[MetaOapg.properties.nu, decimal.Decimal, int, float, ],
        raan: typing.Union[MetaOapg.properties.raan, decimal.Decimal, int, float, ],
        om: typing.Union[MetaOapg.properties.om, decimal.Decimal, int, float, ],
        inc: typing.Union[MetaOapg.properties.inc, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ISDPOrbitalElements':
        return super().__new__(
            cls,
            *args,
            a=a,
            e=e,
            nu=nu,
            raan=raan,
            om=om,
            inc=inc,
            _configuration=_configuration,
            **kwargs,
        )