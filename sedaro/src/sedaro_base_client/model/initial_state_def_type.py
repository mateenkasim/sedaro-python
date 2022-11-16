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


class InitialStateDefType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An enumeration.
    """


    class MetaOapg:
        enum_value_to_name = {
            "ORBITAL_ELEMENTS": "ORBITAL_ELEMENTS",
            "REF_ORBIT": "REF_ORBIT",
            "ECI_STATE": "ECI_STATE",
            "TLE": "TLE",
            "": "EMPTY",
        }
    
    @schemas.classproperty
    def ORBITAL_ELEMENTS(cls):
        return cls("ORBITAL_ELEMENTS")
    
    @schemas.classproperty
    def REF_ORBIT(cls):
        return cls("REF_ORBIT")
    
    @schemas.classproperty
    def ECI_STATE(cls):
        return cls("ECI_STATE")
    
    @schemas.classproperty
    def TLE(cls):
        return cls("TLE")
    
    @schemas.classproperty
    def EMPTY(cls):
        return cls("")
