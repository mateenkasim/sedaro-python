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


class OperationalModeUpdate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "pointingMode",
            "name",
            "priority",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class priority(
                schemas.IntSchema
            ):
                pass
            pointingMode = schemas.StrSchema
            id = schemas.StrSchema
            
            
            class minOccurrenceDuration(
                schemas.NumberSchema
            ):
                pass
            
            
            class maxOccurrenceDuration(
                schemas.NumberSchema
            ):
                pass
            
            
            class minTimeBetweenOccurrences(
                schemas.NumberSchema
            ):
                pass
            
            
            class conditions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'conditions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "priority": priority,
                "pointingMode": pointingMode,
                "id": id,
                "minOccurrenceDuration": minOccurrenceDuration,
                "maxOccurrenceDuration": maxOccurrenceDuration,
                "minTimeBetweenOccurrences": minTimeBetweenOccurrences,
                "conditions": conditions,
            }
    
    pointingMode: MetaOapg.properties.pointingMode
    name: MetaOapg.properties.name
    priority: MetaOapg.properties.priority
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pointingMode"]) -> MetaOapg.properties.pointingMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minOccurrenceDuration"]) -> MetaOapg.properties.minOccurrenceDuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxOccurrenceDuration"]) -> MetaOapg.properties.maxOccurrenceDuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minTimeBetweenOccurrences"]) -> MetaOapg.properties.minTimeBetweenOccurrences: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions"]) -> MetaOapg.properties.conditions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "priority", "pointingMode", "id", "minOccurrenceDuration", "maxOccurrenceDuration", "minTimeBetweenOccurrences", "conditions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pointingMode"]) -> MetaOapg.properties.pointingMode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minOccurrenceDuration"]) -> typing.Union[MetaOapg.properties.minOccurrenceDuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxOccurrenceDuration"]) -> typing.Union[MetaOapg.properties.maxOccurrenceDuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minTimeBetweenOccurrences"]) -> typing.Union[MetaOapg.properties.minTimeBetweenOccurrences, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions"]) -> typing.Union[MetaOapg.properties.conditions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "priority", "pointingMode", "id", "minOccurrenceDuration", "maxOccurrenceDuration", "minTimeBetweenOccurrences", "conditions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        pointingMode: typing.Union[MetaOapg.properties.pointingMode, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        priority: typing.Union[MetaOapg.properties.priority, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        minOccurrenceDuration: typing.Union[MetaOapg.properties.minOccurrenceDuration, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        maxOccurrenceDuration: typing.Union[MetaOapg.properties.maxOccurrenceDuration, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        minTimeBetweenOccurrences: typing.Union[MetaOapg.properties.minTimeBetweenOccurrences, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        conditions: typing.Union[MetaOapg.properties.conditions, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OperationalModeUpdate':
        return super().__new__(
            cls,
            *args,
            pointingMode=pointingMode,
            name=name,
            priority=priority,
            id=id,
            minOccurrenceDuration=minOccurrenceDuration,
            maxOccurrenceDuration=maxOccurrenceDuration,
            minTimeBetweenOccurrences=minTimeBetweenOccurrences,
            conditions=conditions,
            _configuration=_configuration,
            **kwargs,
        )
