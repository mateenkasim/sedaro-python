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


class TopologyTypes(
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
            "SINGLE_CONV_MPPT": "SINGLE_CONV_MPPT",
            "TWO_CONV_MPPT": "TWO_CONV_MPPT",
            "QUASI_REG_DET": "QUASI_REG_DET",
            "FULLY_REG_DET": "FULLY_REG_DET",
            "SINGLE_CONV_HYBRID": "SINGLE_CONV_HYBRID",
        }
    
    @schemas.classproperty
    def SINGLE_CONV_MPPT(cls):
        return cls("SINGLE_CONV_MPPT")
    
    @schemas.classproperty
    def TWO_CONV_MPPT(cls):
        return cls("TWO_CONV_MPPT")
    
    @schemas.classproperty
    def QUASI_REG_DET(cls):
        return cls("QUASI_REG_DET")
    
    @schemas.classproperty
    def FULLY_REG_DET(cls):
        return cls("FULLY_REG_DET")
    
    @schemas.classproperty
    def SINGLE_CONV_HYBRID(cls):
        return cls("SINGLE_CONV_HYBRID")
