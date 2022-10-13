# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import sedaro_base_client
from sedaro_base_client.paths.models_branches_branch_id_system_geometry_surfaces_ import post  # noqa: E501
from sedaro_base_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestModelsBranchesBranchIdSystemGeometrySurfaces(ApiTestMixin, unittest.TestCase):
    """
    ModelsBranchesBranchIdSystemGeometrySurfaces unit test stubs
        Create Surface  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
