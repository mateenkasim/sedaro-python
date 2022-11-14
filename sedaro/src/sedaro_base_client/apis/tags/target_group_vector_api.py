# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).   # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""

from sedaro_base_client.paths.models_branches_branch_id_gnc_reference_vectors_target_group_vectors_.post import CreateTargetGroupVector
from sedaro_base_client.paths.models_branches_branch_id_gnc_reference_vectors_target_group_vectors_block_id.delete import DeleteTargetGroupVector
from sedaro_base_client.paths.models_branches_branch_id_gnc_reference_vectors_target_group_vectors_block_id.patch import UpdateTargetGroupVector


class TargetGroupVectorApi(
    CreateTargetGroupVector,
    DeleteTargetGroupVector,
    UpdateTargetGroupVector,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass