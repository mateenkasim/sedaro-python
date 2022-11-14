# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).   # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""

from sedaro_base_client.paths.simulations_branches_branch_id_control_job_id.get import GetSimulation
from sedaro_base_client.paths.simulations_branches_branch_id_control_.get import GetSimulations
from sedaro_base_client.paths.simulations_branches_branch_id_control_.post import StartSimulation
from sedaro_base_client.paths.simulations_branches_branch_id_control_job_id.delete import TerminateSimulation


class JobsApi(
    GetSimulation,
    GetSimulations,
    StartSimulation,
    TerminateSimulation,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass