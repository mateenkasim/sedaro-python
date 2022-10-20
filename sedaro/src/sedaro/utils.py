import json
from functools import cache
from pydash.strings import snake_case, pascal_case
from urllib3.response import HTTPResponse
from typing import Dict, Tuple, Union, TYPE_CHECKING

from sedaro_base_client.api_client import ApiResponse
from .settings import DELETE

if TYPE_CHECKING:
    from .branch_client import BranchClient


@cache
def get_snake_and_pascal_case(s: str):
    '''Returns a tuple of the string in snake and pascal case'''
    return snake_case(s), pascal_case(s, strict=False)


def parse_urllib_response(response: HTTPResponse) -> Dict:
    '''Parses the response from urllib3.response.HTTPResponse into a dictionary'''
    return json.loads(response.data.decode('utf-8'))


def parse_block_crud_response(response: ApiResponse) -> Tuple[str, dict, str, str]:
    """Parses the response of CRUD-ing a Sedaro Block on a `Branch` into a tuple.

    Args:
        response (ApiResponse): the response from CRUD-ing a Sedaro Block

    Returns:
        Dict: a tuple of: `block_id`, `block_data`, `block_group`, `action`, `branch_data`, `block_id_to_type_map`
    """
    body = response.body
    action = body['action']
    block_id = body['block']['id']
    block_group = body['block']['group']
    branch_data = body['branch']['data']

    block_data = dict(branch_data[block_group][block_id]) if action.casefold() != DELETE.casefold() \
        else None

    return block_id, block_data, block_group, action, branch_data, body['branch']['blockIdToTypeMap']


@cache
def sanitize_and_enforce_id_in_branch(branch_client: 'BranchClient', id: Union[str, int]):
    """Makes sure `id` is of the right type and exists in the Sedaro Branch associated with the `BranchClient`

    Args:
        branch_client (BranchClient): the `BranchClient` associated with the Sedaro Branch to check for the `id`
        id (Union[str, int]): `id` of the Sedaro Block to sanitize and check

    Raises:
        TypeError: if the `id` is not an integer or an integer string
        KeyError: if no corresponding Block exists in the Branch

    Returns:
        str: the integer string `id` of the Block
    """
    if type(id) == int:
        id = str(id)

    if type(id) is not str or (type(id) is str and not id.isdigit()):
        raise TypeError(
            f'The "id" argument must be an integer or string of an integer, not "{type(id).__name__}".'
        )

    if id not in branch_client._block_id_to_type_map:
        raise KeyError(f'There is no Block with id "{id}" in this Branch.')

    return id
