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


class TargetVector(
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
            "referenceTarget",
        }
        
        class properties:
            name = schemas.StrSchema
            
            
            class vectorType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "TARGET": "TARGET",
                    }
                
                @schemas.classproperty
                def TARGET(cls):
                    return cls("TARGET")
            referenceTarget = schemas.StrSchema
            id = schemas.StrSchema
            
            
            class truth(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'truth':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class estimate(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'estimate':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            eclipsed = schemas.BoolSchema
            
            
            class FOVConstraints(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'FOVConstraints':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class directionSensors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'directionSensors':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class vectorSensors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'vectorSensors':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "vectorType": vectorType,
                "referenceTarget": referenceTarget,
                "id": id,
                "truth": truth,
                "estimate": estimate,
                "eclipsed": eclipsed,
                "FOVConstraints": FOVConstraints,
                "directionSensors": directionSensors,
                "vectorSensors": vectorSensors,
            }
    
    vectorType: MetaOapg.properties.vectorType
    name: MetaOapg.properties.name
    referenceTarget: MetaOapg.properties.referenceTarget
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vectorType"]) -> MetaOapg.properties.vectorType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referenceTarget"]) -> MetaOapg.properties.referenceTarget: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["truth"]) -> MetaOapg.properties.truth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["estimate"]) -> MetaOapg.properties.estimate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eclipsed"]) -> MetaOapg.properties.eclipsed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FOVConstraints"]) -> MetaOapg.properties.FOVConstraints: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["directionSensors"]) -> MetaOapg.properties.directionSensors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vectorSensors"]) -> MetaOapg.properties.vectorSensors: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "vectorType", "referenceTarget", "id", "truth", "estimate", "eclipsed", "FOVConstraints", "directionSensors", "vectorSensors", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vectorType"]) -> MetaOapg.properties.vectorType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referenceTarget"]) -> MetaOapg.properties.referenceTarget: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["truth"]) -> typing.Union[MetaOapg.properties.truth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["estimate"]) -> typing.Union[MetaOapg.properties.estimate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eclipsed"]) -> typing.Union[MetaOapg.properties.eclipsed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FOVConstraints"]) -> typing.Union[MetaOapg.properties.FOVConstraints, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["directionSensors"]) -> typing.Union[MetaOapg.properties.directionSensors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vectorSensors"]) -> typing.Union[MetaOapg.properties.vectorSensors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "vectorType", "referenceTarget", "id", "truth", "estimate", "eclipsed", "FOVConstraints", "directionSensors", "vectorSensors", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        vectorType: typing.Union[MetaOapg.properties.vectorType, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        referenceTarget: typing.Union[MetaOapg.properties.referenceTarget, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        truth: typing.Union[MetaOapg.properties.truth, list, tuple, schemas.Unset] = schemas.unset,
        estimate: typing.Union[MetaOapg.properties.estimate, list, tuple, schemas.Unset] = schemas.unset,
        eclipsed: typing.Union[MetaOapg.properties.eclipsed, bool, schemas.Unset] = schemas.unset,
        FOVConstraints: typing.Union[MetaOapg.properties.FOVConstraints, list, tuple, schemas.Unset] = schemas.unset,
        directionSensors: typing.Union[MetaOapg.properties.directionSensors, list, tuple, schemas.Unset] = schemas.unset,
        vectorSensors: typing.Union[MetaOapg.properties.vectorSensors, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TargetVector':
        return super().__new__(
            cls,
            *args,
            vectorType=vectorType,
            name=name,
            referenceTarget=referenceTarget,
            id=id,
            truth=truth,
            estimate=estimate,
            eclipsed=eclipsed,
            FOVConstraints=FOVConstraints,
            directionSensors=directionSensors,
            vectorSensors=vectorSensors,
            _configuration=_configuration,
            **kwargs,
        )
