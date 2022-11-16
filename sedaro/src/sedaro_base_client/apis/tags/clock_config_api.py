# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com   # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""

from sedaro_base_client.paths.models_branches_branch_id_clock_configs_.post import CreateClockConfig
from sedaro_base_client.paths.models_branches_branch_id_clock_configs_block_id.delete import DeleteClockConfig
from sedaro_base_client.paths.models_branches_branch_id_clock_configs_block_id.patch import UpdateClockConfig


class ClockConfigApi(
    CreateClockConfig,
    DeleteClockConfig,
    UpdateClockConfig,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
