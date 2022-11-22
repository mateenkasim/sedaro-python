# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).   # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""

from sedaro_base_client.paths.models_branches_branch_id_system_subsystems_.post import CreateSubsystem
from sedaro_base_client.paths.models_branches_branch_id_system_subsystems_block_id.delete import DeleteSubsystem
from sedaro_base_client.paths.models_branches_branch_id_system_subsystems_block_id.patch import UpdateSubsystem


class SubsystemApi(
    CreateSubsystem,
    DeleteSubsystem,
    UpdateSubsystem,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
