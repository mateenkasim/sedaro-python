# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Currently the documentation for 200 responses to Block create, read, update, and delete (CRUD) operations is incorrect. This is due to an issue with our documentation generator.  Under each Block Group, the documentation will show `name`, `collection`, and `data` keys.  In reality, this level does not exist and should be skipped.  See the schema under the `data` key of a Template's Block Group for the correct schema of such Block Group. - Error responses are most specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 3.3.4
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


class BatteryCell(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Class to be used internally and inherited only by `Collection` and `Block`. Adds helper methods that help with
relationship fields.
    """


    class MetaOapg:
        required = {
            "curve",
            "esr",
            "topology",
            "partNumber",
            "maxChargeCurrent",
            "maxDischargeCurrent",
            "minSoc",
            "capacity",
        }
        
        class properties:
            
            
            class partNumber(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 32
            
            
            class esr(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            
            
            class maxChargeCurrent(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            
            
            class maxDischargeCurrent(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            
            
            class minSoc(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 1.0
                    inclusive_minimum = 0.0
            
            
            class curve(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 2
                    min_items = 2
                    
                    
                    class items(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class items(
                                schemas.NumberSchema
                            ):
                            
                            
                                class MetaOapg:
                                    inclusive_minimum = 0.0
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, list, tuple, ]], typing.List[typing.Union[MetaOapg.items, list, tuple, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'curve':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class capacity(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            topology = schemas.StrSchema
            id = schemas.StrSchema
            
            
            class manufacturer(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 32
            __annotations__ = {
                "partNumber": partNumber,
                "esr": esr,
                "maxChargeCurrent": maxChargeCurrent,
                "maxDischargeCurrent": maxDischargeCurrent,
                "minSoc": minSoc,
                "curve": curve,
                "capacity": capacity,
                "topology": topology,
                "id": id,
                "manufacturer": manufacturer,
            }
    
    curve: MetaOapg.properties.curve
    esr: MetaOapg.properties.esr
    topology: MetaOapg.properties.topology
    partNumber: MetaOapg.properties.partNumber
    maxChargeCurrent: MetaOapg.properties.maxChargeCurrent
    maxDischargeCurrent: MetaOapg.properties.maxDischargeCurrent
    minSoc: MetaOapg.properties.minSoc
    capacity: MetaOapg.properties.capacity
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partNumber"]) -> MetaOapg.properties.partNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["esr"]) -> MetaOapg.properties.esr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxChargeCurrent"]) -> MetaOapg.properties.maxChargeCurrent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxDischargeCurrent"]) -> MetaOapg.properties.maxDischargeCurrent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minSoc"]) -> MetaOapg.properties.minSoc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["curve"]) -> MetaOapg.properties.curve: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["capacity"]) -> MetaOapg.properties.capacity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topology"]) -> MetaOapg.properties.topology: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["manufacturer"]) -> MetaOapg.properties.manufacturer: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["partNumber", "esr", "maxChargeCurrent", "maxDischargeCurrent", "minSoc", "curve", "capacity", "topology", "id", "manufacturer", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partNumber"]) -> MetaOapg.properties.partNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["esr"]) -> MetaOapg.properties.esr: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxChargeCurrent"]) -> MetaOapg.properties.maxChargeCurrent: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxDischargeCurrent"]) -> MetaOapg.properties.maxDischargeCurrent: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minSoc"]) -> MetaOapg.properties.minSoc: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["curve"]) -> MetaOapg.properties.curve: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["capacity"]) -> MetaOapg.properties.capacity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topology"]) -> MetaOapg.properties.topology: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["manufacturer"]) -> typing.Union[MetaOapg.properties.manufacturer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["partNumber", "esr", "maxChargeCurrent", "maxDischargeCurrent", "minSoc", "curve", "capacity", "topology", "id", "manufacturer", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        curve: typing.Union[MetaOapg.properties.curve, list, tuple, ],
        esr: typing.Union[MetaOapg.properties.esr, decimal.Decimal, int, float, ],
        topology: typing.Union[MetaOapg.properties.topology, str, ],
        partNumber: typing.Union[MetaOapg.properties.partNumber, str, ],
        maxChargeCurrent: typing.Union[MetaOapg.properties.maxChargeCurrent, decimal.Decimal, int, float, ],
        maxDischargeCurrent: typing.Union[MetaOapg.properties.maxDischargeCurrent, decimal.Decimal, int, float, ],
        minSoc: typing.Union[MetaOapg.properties.minSoc, decimal.Decimal, int, float, ],
        capacity: typing.Union[MetaOapg.properties.capacity, decimal.Decimal, int, float, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        manufacturer: typing.Union[MetaOapg.properties.manufacturer, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BatteryCell':
        return super().__new__(
            cls,
            *_args,
            curve=curve,
            esr=esr,
            topology=topology,
            partNumber=partNumber,
            maxChargeCurrent=maxChargeCurrent,
            maxDischargeCurrent=maxDischargeCurrent,
            minSoc=minSoc,
            capacity=capacity,
            id=id,
            manufacturer=manufacturer,
            _configuration=_configuration,
            **kwargs,
        )
