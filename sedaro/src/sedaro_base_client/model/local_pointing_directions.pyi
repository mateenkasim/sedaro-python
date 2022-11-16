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


class LocalPointingDirections(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An enumeration.
    """
    
    @schemas.classproperty
    def NADIR(cls):
        return cls("NADIR")
    
    @schemas.classproperty
    def ZENITH(cls):
        return cls("ZENITH")
    
    @schemas.classproperty
    def CROSS_TRACK_POS(cls):
        return cls("CROSS_TRACK_POS")
    
    @schemas.classproperty
    def CROSS_TRACK_NEG(cls):
        return cls("CROSS_TRACK_NEG")
    
    @schemas.classproperty
    def ALONG_TRACK_POS(cls):
        return cls("ALONG_TRACK_POS")
    
    @schemas.classproperty
    def ALONG_TRACK_NEG(cls):
        return cls("ALONG_TRACK_NEG")
    
    @schemas.classproperty
    def RAM(cls):
        return cls("RAM")
    
    @schemas.classproperty
    def ANTI_RAM(cls):
        return cls("ANTI_RAM")
    
    @schemas.classproperty
    def MAGNETIC_FIELD(cls):
        return cls("MAGNETIC_FIELD")
    
    @schemas.classproperty
    def EMPTY(cls):
        return cls("")
