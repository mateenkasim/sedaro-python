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


class SphericalAngles(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "phi",
            "theta",
        }
        
        class properties:
            
            
            class theta(
                schemas.NumberSchema
            ):
                pass
            
            
            class phi(
                schemas.NumberSchema
            ):
                pass
            __annotations__ = {
                "theta": theta,
                "phi": phi,
            }
    
    phi: MetaOapg.properties.phi
    theta: MetaOapg.properties.theta
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["theta"]) -> MetaOapg.properties.theta: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phi"]) -> MetaOapg.properties.phi: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["theta", "phi", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["theta"]) -> MetaOapg.properties.theta: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phi"]) -> MetaOapg.properties.phi: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["theta", "phi", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        phi: typing.Union[MetaOapg.properties.phi, decimal.Decimal, int, float, ],
        theta: typing.Union[MetaOapg.properties.theta, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SphericalAngles':
        return super().__new__(
            cls,
            *args,
            phi=phi,
            theta=theta,
            _configuration=_configuration,
            **kwargs,
        )
