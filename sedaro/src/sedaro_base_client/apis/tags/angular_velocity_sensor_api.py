# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).   # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""

from sedaro_base_client.paths.models_branches_branch_id_gnc_sensors_angular_velocity_sensors_.post import CreateAngularVelocitySensor
from sedaro_base_client.paths.models_branches_branch_id_gnc_sensors_angular_velocity_sensors_block_id.delete import DeleteAngularVelocitySensor
from sedaro_base_client.paths.models_branches_branch_id_gnc_sensors_angular_velocity_sensors_block_id.patch import UpdateAngularVelocitySensor


class AngularVelocitySensorApi(
    CreateAngularVelocitySensor,
    DeleteAngularVelocitySensor,
    UpdateAngularVelocitySensor,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass