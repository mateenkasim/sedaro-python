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


class ClockConfigCreate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "startTime",
            "stopTime",
        }
        
        class properties:
            startTime = schemas.NumberSchema
            stopTime = schemas.NumberSchema
            id = schemas.StrSchema
            realTime = schemas.BoolSchema
            __annotations__ = {
                "startTime": startTime,
                "stopTime": stopTime,
                "id": id,
                "realTime": realTime,
            }
    
    startTime: MetaOapg.properties.startTime
    stopTime: MetaOapg.properties.stopTime
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startTime"]) -> MetaOapg.properties.startTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stopTime"]) -> MetaOapg.properties.stopTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["realTime"]) -> MetaOapg.properties.realTime: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["startTime", "stopTime", "id", "realTime", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startTime"]) -> MetaOapg.properties.startTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stopTime"]) -> MetaOapg.properties.stopTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["realTime"]) -> typing.Union[MetaOapg.properties.realTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["startTime", "stopTime", "id", "realTime", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        startTime: typing.Union[MetaOapg.properties.startTime, decimal.Decimal, int, float, ],
        stopTime: typing.Union[MetaOapg.properties.stopTime, decimal.Decimal, int, float, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        realTime: typing.Union[MetaOapg.properties.realTime, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ClockConfigCreate':
        return super().__new__(
            cls,
            *args,
            startTime=startTime,
            stopTime=stopTime,
            id=id,
            realTime=realTime,
            _configuration=_configuration,
            **kwargs,
        )
