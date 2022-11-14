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


class TargetGroup(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
            "targetType",
            "conOps",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 32
            
            
            class targetType(
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
                            Types,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'targetType':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            conOps = schemas.StrSchema
            id = schemas.StrSchema
            targetAssociations = schemas.DictSchema
            
            
            class targets(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'targets':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class targetGroupVectors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'targetGroupVectors':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class groupConditions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'groupConditions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            activeTarget = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "targetType": targetType,
                "conOps": conOps,
                "id": id,
                "targetAssociations": targetAssociations,
                "targets": targets,
                "targetGroupVectors": targetGroupVectors,
                "groupConditions": groupConditions,
                "activeTarget": activeTarget,
            }
    
    name: MetaOapg.properties.name
    targetType: MetaOapg.properties.targetType
    conOps: MetaOapg.properties.conOps
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetType"]) -> MetaOapg.properties.targetType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conOps"]) -> MetaOapg.properties.conOps: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetAssociations"]) -> MetaOapg.properties.targetAssociations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targets"]) -> MetaOapg.properties.targets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetGroupVectors"]) -> MetaOapg.properties.targetGroupVectors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupConditions"]) -> MetaOapg.properties.groupConditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activeTarget"]) -> MetaOapg.properties.activeTarget: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "targetType", "conOps", "id", "targetAssociations", "targets", "targetGroupVectors", "groupConditions", "activeTarget", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetType"]) -> MetaOapg.properties.targetType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conOps"]) -> MetaOapg.properties.conOps: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetAssociations"]) -> typing.Union[MetaOapg.properties.targetAssociations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targets"]) -> typing.Union[MetaOapg.properties.targets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetGroupVectors"]) -> typing.Union[MetaOapg.properties.targetGroupVectors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupConditions"]) -> typing.Union[MetaOapg.properties.groupConditions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activeTarget"]) -> typing.Union[MetaOapg.properties.activeTarget, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "targetType", "conOps", "id", "targetAssociations", "targets", "targetGroupVectors", "groupConditions", "activeTarget", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        targetType: typing.Union[MetaOapg.properties.targetType, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        conOps: typing.Union[MetaOapg.properties.conOps, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        targetAssociations: typing.Union[MetaOapg.properties.targetAssociations, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        targets: typing.Union[MetaOapg.properties.targets, list, tuple, schemas.Unset] = schemas.unset,
        targetGroupVectors: typing.Union[MetaOapg.properties.targetGroupVectors, list, tuple, schemas.Unset] = schemas.unset,
        groupConditions: typing.Union[MetaOapg.properties.groupConditions, list, tuple, schemas.Unset] = schemas.unset,
        activeTarget: typing.Union[MetaOapg.properties.activeTarget, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TargetGroup':
        return super().__new__(
            cls,
            *args,
            name=name,
            targetType=targetType,
            conOps=conOps,
            id=id,
            targetAssociations=targetAssociations,
            targets=targets,
            targetGroupVectors=targetGroupVectors,
            groupConditions=groupConditions,
            activeTarget=activeTarget,
            _configuration=_configuration,
            **kwargs,
        )

from sedaro_base_client.model.types import Types