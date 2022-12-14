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


class MEKFAlgorithmCreate(
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
            "algorithmType",
            "rate",
            "name",
            "algorithmSubtype",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            rate = schemas.NumberSchema
            
            
            class algorithmType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ATTITUDE_DETERMINATION": "ATTITUDE_DETERMINATION",
                    }
                
                @schemas.classproperty
                def ATTITUDE_DETERMINATION(cls):
                    return cls("ATTITUDE_DETERMINATION")
            
            
            class algorithmSubtype(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "MEKF": "MEKF",
                    }
                
                @schemas.classproperty
                def MEKF(cls):
                    return cls("MEKF")
            id = schemas.StrSchema
            satellite = schemas.StrSchema
            
            
            class attitudeSolution(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'attitudeSolution':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class angularVelocitySolution(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'angularVelocitySolution':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            covariance = schemas.AnyTypeSchema
            
            
            class opticalAttitudeSensors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'opticalAttitudeSensors':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class angularVelocitySensors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'angularVelocitySensors':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "rate": rate,
                "algorithmType": algorithmType,
                "algorithmSubtype": algorithmSubtype,
                "id": id,
                "satellite": satellite,
                "attitudeSolution": attitudeSolution,
                "angularVelocitySolution": angularVelocitySolution,
                "covariance": covariance,
                "opticalAttitudeSensors": opticalAttitudeSensors,
                "angularVelocitySensors": angularVelocitySensors,
            }
    
    algorithmType: MetaOapg.properties.algorithmType
    rate: MetaOapg.properties.rate
    name: MetaOapg.properties.name
    algorithmSubtype: MetaOapg.properties.algorithmSubtype
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rate"]) -> MetaOapg.properties.rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["algorithmType"]) -> MetaOapg.properties.algorithmType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["algorithmSubtype"]) -> MetaOapg.properties.algorithmSubtype: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["satellite"]) -> MetaOapg.properties.satellite: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attitudeSolution"]) -> MetaOapg.properties.attitudeSolution: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["angularVelocitySolution"]) -> MetaOapg.properties.angularVelocitySolution: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["covariance"]) -> MetaOapg.properties.covariance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["opticalAttitudeSensors"]) -> MetaOapg.properties.opticalAttitudeSensors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["angularVelocitySensors"]) -> MetaOapg.properties.angularVelocitySensors: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "rate", "algorithmType", "algorithmSubtype", "id", "satellite", "attitudeSolution", "angularVelocitySolution", "covariance", "opticalAttitudeSensors", "angularVelocitySensors", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rate"]) -> MetaOapg.properties.rate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["algorithmType"]) -> MetaOapg.properties.algorithmType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["algorithmSubtype"]) -> MetaOapg.properties.algorithmSubtype: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["satellite"]) -> typing.Union[MetaOapg.properties.satellite, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attitudeSolution"]) -> typing.Union[MetaOapg.properties.attitudeSolution, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["angularVelocitySolution"]) -> typing.Union[MetaOapg.properties.angularVelocitySolution, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["covariance"]) -> typing.Union[MetaOapg.properties.covariance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["opticalAttitudeSensors"]) -> typing.Union[MetaOapg.properties.opticalAttitudeSensors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["angularVelocitySensors"]) -> typing.Union[MetaOapg.properties.angularVelocitySensors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "rate", "algorithmType", "algorithmSubtype", "id", "satellite", "attitudeSolution", "angularVelocitySolution", "covariance", "opticalAttitudeSensors", "angularVelocitySensors", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        algorithmType: typing.Union[MetaOapg.properties.algorithmType, str, ],
        rate: typing.Union[MetaOapg.properties.rate, decimal.Decimal, int, float, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        algorithmSubtype: typing.Union[MetaOapg.properties.algorithmSubtype, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        satellite: typing.Union[MetaOapg.properties.satellite, str, schemas.Unset] = schemas.unset,
        attitudeSolution: typing.Union[MetaOapg.properties.attitudeSolution, list, tuple, schemas.Unset] = schemas.unset,
        angularVelocitySolution: typing.Union[MetaOapg.properties.angularVelocitySolution, list, tuple, schemas.Unset] = schemas.unset,
        covariance: typing.Union[MetaOapg.properties.covariance, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        opticalAttitudeSensors: typing.Union[MetaOapg.properties.opticalAttitudeSensors, list, tuple, schemas.Unset] = schemas.unset,
        angularVelocitySensors: typing.Union[MetaOapg.properties.angularVelocitySensors, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MEKFAlgorithmCreate':
        return super().__new__(
            cls,
            *_args,
            algorithmType=algorithmType,
            rate=rate,
            name=name,
            algorithmSubtype=algorithmSubtype,
            id=id,
            satellite=satellite,
            attitudeSolution=attitudeSolution,
            angularVelocitySolution=angularVelocitySolution,
            covariance=covariance,
            opticalAttitudeSensors=opticalAttitudeSensors,
            angularVelocitySensors=angularVelocitySensors,
            _configuration=_configuration,
            **kwargs,
        )
