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


class LocalPointingDirections(
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
            "NADIR": "NADIR",
            "ZENITH": "ZENITH",
            "CROSS_TRACK_POS": "CROSS_TRACK_POS",
            "CROSS_TRACK_NEG": "CROSS_TRACK_NEG",
            "ALONG_TRACK_POS": "ALONG_TRACK_POS",
            "ALONG_TRACK_NEG": "ALONG_TRACK_NEG",
            "RAM": "RAM",
            "ANTI_RAM": "ANTI_RAM",
            "MAGNETIC_FIELD": "MAGNETIC_FIELD",
            "": "EMPTY",
        }
    
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
