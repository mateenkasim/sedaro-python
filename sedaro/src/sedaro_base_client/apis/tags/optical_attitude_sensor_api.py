# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).   # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""

from sedaro_base_client.paths.models_branches_branch_id_gnc_sensors_optical_attitude_sensors_.post import CreateOpticalAttitudeSensor
from sedaro_base_client.paths.models_branches_branch_id_gnc_sensors_optical_attitude_sensors_block_id.delete import DeleteOpticalAttitudeSensor
from sedaro_base_client.paths.models_branches_branch_id_gnc_sensors_optical_attitude_sensors_block_id.patch import UpdateOpticalAttitudeSensor


class OpticalAttitudeSensorApi(
    CreateOpticalAttitudeSensor,
    DeleteOpticalAttitudeSensor,
    UpdateOpticalAttitudeSensor,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass