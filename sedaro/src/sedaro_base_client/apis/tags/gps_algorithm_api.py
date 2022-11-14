# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).   # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""

from sedaro_base_client.paths.models_branches_branch_id_gnc_algorithms_orbit_determination_gps_.post import CreateGpsAlgorithm
from sedaro_base_client.paths.models_branches_branch_id_gnc_algorithms_orbit_determination_gps_block_id.delete import DeleteGpsAlgorithm
from sedaro_base_client.paths.models_branches_branch_id_gnc_algorithms_orbit_determination_gps_block_id.patch import UpdateGpsAlgorithm


class GPSAlgorithmApi(
    CreateGpsAlgorithm,
    DeleteGpsAlgorithm,
    UpdateGpsAlgorithm,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass