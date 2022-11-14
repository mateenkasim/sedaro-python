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


class TopologyParamQRD(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "bcrEfficiency",
            "chargeDiodeDrop",
            "chargeControllerBusVoltage",
            "dischargeDiodeDrop",
            "outputPowerRating",
        }
        
        class properties:
            
            
            class bcrEfficiency(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 1.0
            
            
            class outputPowerRating(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            
            
            class chargeDiodeDrop(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            
            
            class dischargeDiodeDrop(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            
            
            class chargeControllerBusVoltage(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            __annotations__ = {
                "bcrEfficiency": bcrEfficiency,
                "outputPowerRating": outputPowerRating,
                "chargeDiodeDrop": chargeDiodeDrop,
                "dischargeDiodeDrop": dischargeDiodeDrop,
                "chargeControllerBusVoltage": chargeControllerBusVoltage,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    bcrEfficiency: MetaOapg.properties.bcrEfficiency
    chargeDiodeDrop: MetaOapg.properties.chargeDiodeDrop
    chargeControllerBusVoltage: MetaOapg.properties.chargeControllerBusVoltage
    dischargeDiodeDrop: MetaOapg.properties.dischargeDiodeDrop
    outputPowerRating: MetaOapg.properties.outputPowerRating
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bcrEfficiency"]) -> MetaOapg.properties.bcrEfficiency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chargeDiodeDrop"]) -> MetaOapg.properties.chargeDiodeDrop: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chargeControllerBusVoltage"]) -> MetaOapg.properties.chargeControllerBusVoltage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dischargeDiodeDrop"]) -> MetaOapg.properties.dischargeDiodeDrop: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outputPowerRating"]) -> MetaOapg.properties.outputPowerRating: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bcrEfficiency"], typing_extensions.Literal["chargeDiodeDrop"], typing_extensions.Literal["chargeControllerBusVoltage"], typing_extensions.Literal["dischargeDiodeDrop"], typing_extensions.Literal["outputPowerRating"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bcrEfficiency"]) -> MetaOapg.properties.bcrEfficiency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chargeDiodeDrop"]) -> MetaOapg.properties.chargeDiodeDrop: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chargeControllerBusVoltage"]) -> MetaOapg.properties.chargeControllerBusVoltage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dischargeDiodeDrop"]) -> MetaOapg.properties.dischargeDiodeDrop: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outputPowerRating"]) -> MetaOapg.properties.outputPowerRating: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bcrEfficiency"], typing_extensions.Literal["chargeDiodeDrop"], typing_extensions.Literal["chargeControllerBusVoltage"], typing_extensions.Literal["dischargeDiodeDrop"], typing_extensions.Literal["outputPowerRating"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bcrEfficiency: typing.Union[MetaOapg.properties.bcrEfficiency, decimal.Decimal, int, float, ],
        chargeDiodeDrop: typing.Union[MetaOapg.properties.chargeDiodeDrop, decimal.Decimal, int, float, ],
        chargeControllerBusVoltage: typing.Union[MetaOapg.properties.chargeControllerBusVoltage, decimal.Decimal, int, float, ],
        dischargeDiodeDrop: typing.Union[MetaOapg.properties.dischargeDiodeDrop, decimal.Decimal, int, float, ],
        outputPowerRating: typing.Union[MetaOapg.properties.outputPowerRating, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TopologyParamQRD':
        return super().__new__(
            cls,
            *args,
            bcrEfficiency=bcrEfficiency,
            chargeDiodeDrop=chargeDiodeDrop,
            chargeControllerBusVoltage=chargeControllerBusVoltage,
            dischargeDiodeDrop=dischargeDiodeDrop,
            outputPowerRating=outputPowerRating,
            _configuration=_configuration,
        )