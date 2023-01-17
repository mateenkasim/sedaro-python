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


class MaxAlignPointingMode(
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
            "lockBodyFrameVector",
            "name",
            "pointingModeType",
            "acAlgorithm",
            "conOps",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class pointingModeType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def MAX_SECONDARY_ALIGN(cls):
                    return cls("MAX_SECONDARY_ALIGN")
            conOps = schemas.StrSchema
            lockBodyFrameVector = schemas.StrSchema
            acAlgorithm = schemas.StrSchema
            id = schemas.StrSchema
            odAlgorithm = schemas.StrSchema
            adAlgorithm = schemas.StrSchema
            tcAlgorithm = schemas.StrSchema
            
            
            class operationalModes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'operationalModes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class reactionWheelCommands(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'reactionWheelCommands':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class magnetorquerCommands(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'magnetorquerCommands':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            commandedAttitude = schemas.AnyTypeSchema
            commandedAngularRates = schemas.AnyTypeSchema
            lockVector = schemas.StrSchema
            maxAlignBodyFrameVector = schemas.StrSchema
            maxAlignVector = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "pointingModeType": pointingModeType,
                "conOps": conOps,
                "lockBodyFrameVector": lockBodyFrameVector,
                "acAlgorithm": acAlgorithm,
                "id": id,
                "odAlgorithm": odAlgorithm,
                "adAlgorithm": adAlgorithm,
                "tcAlgorithm": tcAlgorithm,
                "operationalModes": operationalModes,
                "reactionWheelCommands": reactionWheelCommands,
                "magnetorquerCommands": magnetorquerCommands,
                "commandedAttitude": commandedAttitude,
                "commandedAngularRates": commandedAngularRates,
                "lockVector": lockVector,
                "maxAlignBodyFrameVector": maxAlignBodyFrameVector,
                "maxAlignVector": maxAlignVector,
            }
    
    lockBodyFrameVector: MetaOapg.properties.lockBodyFrameVector
    name: MetaOapg.properties.name
    pointingModeType: MetaOapg.properties.pointingModeType
    acAlgorithm: MetaOapg.properties.acAlgorithm
    conOps: MetaOapg.properties.conOps
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pointingModeType"]) -> MetaOapg.properties.pointingModeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conOps"]) -> MetaOapg.properties.conOps: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lockBodyFrameVector"]) -> MetaOapg.properties.lockBodyFrameVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["acAlgorithm"]) -> MetaOapg.properties.acAlgorithm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["odAlgorithm"]) -> MetaOapg.properties.odAlgorithm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["adAlgorithm"]) -> MetaOapg.properties.adAlgorithm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tcAlgorithm"]) -> MetaOapg.properties.tcAlgorithm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operationalModes"]) -> MetaOapg.properties.operationalModes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reactionWheelCommands"]) -> MetaOapg.properties.reactionWheelCommands: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["magnetorquerCommands"]) -> MetaOapg.properties.magnetorquerCommands: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commandedAttitude"]) -> MetaOapg.properties.commandedAttitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commandedAngularRates"]) -> MetaOapg.properties.commandedAngularRates: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lockVector"]) -> MetaOapg.properties.lockVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxAlignBodyFrameVector"]) -> MetaOapg.properties.maxAlignBodyFrameVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxAlignVector"]) -> MetaOapg.properties.maxAlignVector: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "pointingModeType", "conOps", "lockBodyFrameVector", "acAlgorithm", "id", "odAlgorithm", "adAlgorithm", "tcAlgorithm", "operationalModes", "reactionWheelCommands", "magnetorquerCommands", "commandedAttitude", "commandedAngularRates", "lockVector", "maxAlignBodyFrameVector", "maxAlignVector", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pointingModeType"]) -> MetaOapg.properties.pointingModeType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conOps"]) -> MetaOapg.properties.conOps: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lockBodyFrameVector"]) -> MetaOapg.properties.lockBodyFrameVector: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["acAlgorithm"]) -> MetaOapg.properties.acAlgorithm: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["odAlgorithm"]) -> typing.Union[MetaOapg.properties.odAlgorithm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["adAlgorithm"]) -> typing.Union[MetaOapg.properties.adAlgorithm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tcAlgorithm"]) -> typing.Union[MetaOapg.properties.tcAlgorithm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operationalModes"]) -> typing.Union[MetaOapg.properties.operationalModes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reactionWheelCommands"]) -> typing.Union[MetaOapg.properties.reactionWheelCommands, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["magnetorquerCommands"]) -> typing.Union[MetaOapg.properties.magnetorquerCommands, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commandedAttitude"]) -> typing.Union[MetaOapg.properties.commandedAttitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commandedAngularRates"]) -> typing.Union[MetaOapg.properties.commandedAngularRates, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lockVector"]) -> typing.Union[MetaOapg.properties.lockVector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxAlignBodyFrameVector"]) -> typing.Union[MetaOapg.properties.maxAlignBodyFrameVector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxAlignVector"]) -> typing.Union[MetaOapg.properties.maxAlignVector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "pointingModeType", "conOps", "lockBodyFrameVector", "acAlgorithm", "id", "odAlgorithm", "adAlgorithm", "tcAlgorithm", "operationalModes", "reactionWheelCommands", "magnetorquerCommands", "commandedAttitude", "commandedAngularRates", "lockVector", "maxAlignBodyFrameVector", "maxAlignVector", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        lockBodyFrameVector: typing.Union[MetaOapg.properties.lockBodyFrameVector, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        pointingModeType: typing.Union[MetaOapg.properties.pointingModeType, str, ],
        acAlgorithm: typing.Union[MetaOapg.properties.acAlgorithm, str, ],
        conOps: typing.Union[MetaOapg.properties.conOps, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        odAlgorithm: typing.Union[MetaOapg.properties.odAlgorithm, str, schemas.Unset] = schemas.unset,
        adAlgorithm: typing.Union[MetaOapg.properties.adAlgorithm, str, schemas.Unset] = schemas.unset,
        tcAlgorithm: typing.Union[MetaOapg.properties.tcAlgorithm, str, schemas.Unset] = schemas.unset,
        operationalModes: typing.Union[MetaOapg.properties.operationalModes, list, tuple, schemas.Unset] = schemas.unset,
        reactionWheelCommands: typing.Union[MetaOapg.properties.reactionWheelCommands, list, tuple, schemas.Unset] = schemas.unset,
        magnetorquerCommands: typing.Union[MetaOapg.properties.magnetorquerCommands, list, tuple, schemas.Unset] = schemas.unset,
        commandedAttitude: typing.Union[MetaOapg.properties.commandedAttitude, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        commandedAngularRates: typing.Union[MetaOapg.properties.commandedAngularRates, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        lockVector: typing.Union[MetaOapg.properties.lockVector, str, schemas.Unset] = schemas.unset,
        maxAlignBodyFrameVector: typing.Union[MetaOapg.properties.maxAlignBodyFrameVector, str, schemas.Unset] = schemas.unset,
        maxAlignVector: typing.Union[MetaOapg.properties.maxAlignVector, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MaxAlignPointingMode':
        return super().__new__(
            cls,
            *_args,
            lockBodyFrameVector=lockBodyFrameVector,
            name=name,
            pointingModeType=pointingModeType,
            acAlgorithm=acAlgorithm,
            conOps=conOps,
            id=id,
            odAlgorithm=odAlgorithm,
            adAlgorithm=adAlgorithm,
            tcAlgorithm=tcAlgorithm,
            operationalModes=operationalModes,
            reactionWheelCommands=reactionWheelCommands,
            magnetorquerCommands=magnetorquerCommands,
            commandedAttitude=commandedAttitude,
            commandedAngularRates=commandedAngularRates,
            lockVector=lockVector,
            maxAlignBodyFrameVector=maxAlignBodyFrameVector,
            maxAlignVector=maxAlignVector,
            _configuration=_configuration,
            **kwargs,
        )
