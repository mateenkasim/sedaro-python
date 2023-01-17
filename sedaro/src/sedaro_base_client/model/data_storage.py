# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### API Key  To access the Sedaro service via this API, you will need an API key.  You can generate an API key for your account in the  Sedaro [Management Console](https://satellite.sedaro.com/#/account). Once complete, pass the API key in all requests  via the `X_API_KEY` HTTP header.  *API keys grant full access to your account and should never be shared. If you think your API key has been compromised,  you can revoke it in the [Management Console](https://satellite.sedaro.com/#/account).*  ### Jupyter Notebooks  For additional examples of how to use this API for modeling and simulation, see our [Mod-Sim Notebooks](https://github.com/sedaro/modsim-notebooks).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Currently the documentation for 200 responses to Block create, read, update, and delete (CRUD) operations is incorrect. This is due to an issue with our documentation generator.  Under each Block Group, the documentation will show `name`, `collection`, and `data` keys.  In reality, this level does not exist and should be skipped.  See the schema under the `data` key of a Template's Block Group for the correct schema of such Block Group. - Error responses are more specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 3.3.6
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


class DataStorage(
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
            "component",
            "name",
            "maxBitRateRead",
            "maxBitRateWrite",
            "capacity",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            capacity = schemas.IntSchema
            maxBitRateRead = schemas.IntSchema
            maxBitRateWrite = schemas.IntSchema
            component = schemas.StrSchema
            id = schemas.StrSchema
            
            
            class usage(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class additional_properties(
                        schemas.IntSchema
                    ):
                    
                    
                        class MetaOapg:
                            inclusive_minimum = 0
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, decimal.Decimal, int, ],
                ) -> 'usage':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class readRate(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
            
            
            class writeRate(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
            
            
            class fillPercent(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 1.0
                    inclusive_minimum = 0.0
            __annotations__ = {
                "name": name,
                "capacity": capacity,
                "maxBitRateRead": maxBitRateRead,
                "maxBitRateWrite": maxBitRateWrite,
                "component": component,
                "id": id,
                "usage": usage,
                "readRate": readRate,
                "writeRate": writeRate,
                "fillPercent": fillPercent,
            }
    
    component: MetaOapg.properties.component
    name: MetaOapg.properties.name
    maxBitRateRead: MetaOapg.properties.maxBitRateRead
    maxBitRateWrite: MetaOapg.properties.maxBitRateWrite
    capacity: MetaOapg.properties.capacity
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["capacity"]) -> MetaOapg.properties.capacity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxBitRateRead"]) -> MetaOapg.properties.maxBitRateRead: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxBitRateWrite"]) -> MetaOapg.properties.maxBitRateWrite: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["component"]) -> MetaOapg.properties.component: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usage"]) -> MetaOapg.properties.usage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readRate"]) -> MetaOapg.properties.readRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["writeRate"]) -> MetaOapg.properties.writeRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fillPercent"]) -> MetaOapg.properties.fillPercent: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "capacity", "maxBitRateRead", "maxBitRateWrite", "component", "id", "usage", "readRate", "writeRate", "fillPercent", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["capacity"]) -> MetaOapg.properties.capacity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxBitRateRead"]) -> MetaOapg.properties.maxBitRateRead: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxBitRateWrite"]) -> MetaOapg.properties.maxBitRateWrite: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["component"]) -> MetaOapg.properties.component: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usage"]) -> typing.Union[MetaOapg.properties.usage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readRate"]) -> typing.Union[MetaOapg.properties.readRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["writeRate"]) -> typing.Union[MetaOapg.properties.writeRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fillPercent"]) -> typing.Union[MetaOapg.properties.fillPercent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "capacity", "maxBitRateRead", "maxBitRateWrite", "component", "id", "usage", "readRate", "writeRate", "fillPercent", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        component: typing.Union[MetaOapg.properties.component, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        maxBitRateRead: typing.Union[MetaOapg.properties.maxBitRateRead, decimal.Decimal, int, ],
        maxBitRateWrite: typing.Union[MetaOapg.properties.maxBitRateWrite, decimal.Decimal, int, ],
        capacity: typing.Union[MetaOapg.properties.capacity, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        usage: typing.Union[MetaOapg.properties.usage, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        readRate: typing.Union[MetaOapg.properties.readRate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        writeRate: typing.Union[MetaOapg.properties.writeRate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        fillPercent: typing.Union[MetaOapg.properties.fillPercent, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DataStorage':
        return super().__new__(
            cls,
            *_args,
            component=component,
            name=name,
            maxBitRateRead=maxBitRateRead,
            maxBitRateWrite=maxBitRateWrite,
            capacity=capacity,
            id=id,
            usage=usage,
            readRate=readRate,
            writeRate=writeRate,
            fillPercent=fillPercent,
            _configuration=_configuration,
            **kwargs,
        )
