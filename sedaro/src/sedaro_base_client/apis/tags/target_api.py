# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).   # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""

from sedaro_base_client.paths.models_branches_branch_id_cdh_conops_celestial_targets_.post import CreateCelestialTarget
from sedaro_base_client.paths.models_branches_branch_id_cdh_conops_ground_targets_.post import CreateGroundTarget
from sedaro_base_client.paths.models_branches_branch_id_cdh_conops_space_targets_.post import CreateSpaceTarget
from sedaro_base_client.paths.models_branches_branch_id_cdh_conops_celestial_targets_block_id.delete import DeleteCelestialTarget
from sedaro_base_client.paths.models_branches_branch_id_cdh_conops_ground_targets_block_id.delete import DeleteGroundTarget
from sedaro_base_client.paths.models_branches_branch_id_cdh_conops_space_targets_block_id.delete import DeleteSpaceTarget
from sedaro_base_client.paths.models_branches_branch_id_cdh_conops_celestial_targets_block_id.patch import UpdateCelestialTarget
from sedaro_base_client.paths.models_branches_branch_id_cdh_conops_ground_targets_block_id.patch import UpdateGroundTarget
from sedaro_base_client.paths.models_branches_branch_id_cdh_conops_space_targets_block_id.patch import UpdateSpaceTarget


class TargetApi(
    CreateCelestialTarget,
    CreateGroundTarget,
    CreateSpaceTarget,
    DeleteCelestialTarget,
    DeleteGroundTarget,
    DeleteSpaceTarget,
    UpdateCelestialTarget,
    UpdateGroundTarget,
    UpdateSpaceTarget,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass