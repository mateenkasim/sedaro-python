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


class ThermalInterfaceCreate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "area",
            "material",
            "name",
            "sideB",
            "sideA",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            area = schemas.NumberSchema
            
            
            class sideA(
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
                            SideCategories,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'sideA':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class sideB(
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
                            SideCategories,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'sideB':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            material = schemas.StrSchema
            componentA = schemas.StrSchema
            componentB = schemas.StrSchema
            surfaceA = schemas.StrSchema
            surfaceB = schemas.StrSchema
            coolerA = schemas.StrSchema
            coolerB = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "area": area,
                "sideA": sideA,
                "sideB": sideB,
                "material": material,
                "componentA": componentA,
                "componentB": componentB,
                "surfaceA": surfaceA,
                "surfaceB": surfaceB,
                "coolerA": coolerA,
                "coolerB": coolerB,
            }
    
    area: MetaOapg.properties.area
    material: MetaOapg.properties.material
    name: MetaOapg.properties.name
    sideB: MetaOapg.properties.sideB
    sideA: MetaOapg.properties.sideA
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["area"]) -> MetaOapg.properties.area: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sideA"]) -> MetaOapg.properties.sideA: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sideB"]) -> MetaOapg.properties.sideB: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["material"]) -> MetaOapg.properties.material: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["componentA"]) -> MetaOapg.properties.componentA: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["componentB"]) -> MetaOapg.properties.componentB: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surfaceA"]) -> MetaOapg.properties.surfaceA: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surfaceB"]) -> MetaOapg.properties.surfaceB: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coolerA"]) -> MetaOapg.properties.coolerA: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coolerB"]) -> MetaOapg.properties.coolerB: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "area", "sideA", "sideB", "material", "componentA", "componentB", "surfaceA", "surfaceB", "coolerA", "coolerB", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["area"]) -> MetaOapg.properties.area: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sideA"]) -> MetaOapg.properties.sideA: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sideB"]) -> MetaOapg.properties.sideB: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["material"]) -> MetaOapg.properties.material: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["componentA"]) -> typing.Union[MetaOapg.properties.componentA, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["componentB"]) -> typing.Union[MetaOapg.properties.componentB, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surfaceA"]) -> typing.Union[MetaOapg.properties.surfaceA, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surfaceB"]) -> typing.Union[MetaOapg.properties.surfaceB, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coolerA"]) -> typing.Union[MetaOapg.properties.coolerA, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coolerB"]) -> typing.Union[MetaOapg.properties.coolerB, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "area", "sideA", "sideB", "material", "componentA", "componentB", "surfaceA", "surfaceB", "coolerA", "coolerB", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        area: typing.Union[MetaOapg.properties.area, decimal.Decimal, int, float, ],
        material: typing.Union[MetaOapg.properties.material, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        sideB: typing.Union[MetaOapg.properties.sideB, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        sideA: typing.Union[MetaOapg.properties.sideA, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        componentA: typing.Union[MetaOapg.properties.componentA, str, schemas.Unset] = schemas.unset,
        componentB: typing.Union[MetaOapg.properties.componentB, str, schemas.Unset] = schemas.unset,
        surfaceA: typing.Union[MetaOapg.properties.surfaceA, str, schemas.Unset] = schemas.unset,
        surfaceB: typing.Union[MetaOapg.properties.surfaceB, str, schemas.Unset] = schemas.unset,
        coolerA: typing.Union[MetaOapg.properties.coolerA, str, schemas.Unset] = schemas.unset,
        coolerB: typing.Union[MetaOapg.properties.coolerB, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ThermalInterfaceCreate':
        return super().__new__(
            cls,
            *args,
            area=area,
            material=material,
            name=name,
            sideB=sideB,
            sideA=sideA,
            componentA=componentA,
            componentB=componentB,
            surfaceA=surfaceA,
            surfaceB=surfaceB,
            coolerA=coolerA,
            coolerB=coolerB,
            _configuration=_configuration,
            **kwargs,
        )

from sedaro_base_client.model.side_categories import SideCategories
