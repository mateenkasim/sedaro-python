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


class Statuses(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An enumeration.
    """
    
    @schemas.classproperty
    def PENDING(cls):
        return cls("PENDING")
    
    @schemas.classproperty
    def RUNNING(cls):
        return cls("RUNNING")
    
    @schemas.classproperty
    def PAUSED(cls):
        return cls("PAUSED")
    
    @schemas.classproperty
    def TERMINATED(cls):
        return cls("TERMINATED")
    
    @schemas.classproperty
    def FAILED(cls):
        return cls("FAILED")
    
    @schemas.classproperty
    def SUCCEEDED(cls):
        return cls("SUCCEEDED")