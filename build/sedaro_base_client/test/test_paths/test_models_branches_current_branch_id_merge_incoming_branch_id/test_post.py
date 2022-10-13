# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import sedaro_base_client
from sedaro_base_client.paths.models_branches_current_branch_id_merge_incoming_branch_id import post  # noqa: E501
from sedaro_base_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestModelsBranchesCurrentBranchIdMergeIncomingBranchId(ApiTestMixin, unittest.TestCase):
    """
    ModelsBranchesCurrentBranchIdMergeIncomingBranchId unit test stubs
        Merge branch into another branch  # noqa: E501
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
