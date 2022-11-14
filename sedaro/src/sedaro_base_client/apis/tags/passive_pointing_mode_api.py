# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).   # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""

from sedaro_base_client.paths.models_branches_branch_id_gnc_pointing_modes_passive_.post import CreatePassivePointingMode
from sedaro_base_client.paths.models_branches_branch_id_gnc_pointing_modes_passive_block_id.delete import DeletePassivePointingMode
from sedaro_base_client.paths.models_branches_branch_id_gnc_pointing_modes_passive_block_id.patch import UpdatePassivePointingMode


class PassivePointingModeApi(
    CreatePassivePointingMode,
    DeletePassivePointingMode,
    UpdatePassivePointingMode,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass