from importlib import import_module
from dataclasses import dataclass
from sedaro_base_client.api_client import Api
from typing import TYPE_CHECKING, Literal, Tuple, Union, List
from pydash.strings import snake_case
from functools import cached_property

from .settings import CREATE, UPDATE, BASE_PACKAGE_NAME
from .block_client import BlockClient
from .utils import get_snake_and_pascal_case, sanitize_and_enforce_id_in_branch
from .exceptions import NoBlockFoundError

if TYPE_CHECKING:
    from .sedaro_api_client import SedaroApiClient
    from .branch_client import BranchClient


@dataclass
class BlockClassClient:
    '''Class for getting `BlockClient`s associated with Sedaro Blocks of this class type'''
    _block_name: str
    '''Name of the Sedaro Block class this `BlockClassClient` is set up to interact with'''
    _branch_client: 'BranchClient'
    '''The `BranchClient` this `BlockClassClient` is connected to'''

    def __str__(self) -> str:
        return f'BlockClassClient({self._block_name}, branch={self._branch_client.id})'

    def __repr__(self):
        return self.__str__()

    @property
    def _sedaro_client(self) -> 'SedaroApiClient':
        '''The `SedaroApiClient` this `BlockClassClient` was accessed through'''
        return self._branch_client._sedaro_client

    @property
    def _create_class(self) -> type:  # TODO: better type hint
        '''The model class to instantiate with appropriate kwargs when creating a Sedaro Block'''
        return self._get_create_or_update_block_model(CREATE)

    @property
    def _update_class(self) -> type:  # TODO: better type hint
        '''The model class to instantiate with appropriate kwargs when updating a Sedaro Block'''
        return self._get_create_or_update_block_model(UPDATE)

    @property
    def _block_openapi_instance(self) -> Api:
        '''The api instance instantiated with the appropriate `SedaroApiClient` to interact with when CRUDing Blocks'''
        block_snake, block_pascal = get_snake_and_pascal_case(self._block_name)
        block_api_module = import_module(
            f'{BASE_PACKAGE_NAME}.apis.tags.{block_snake}_api')
        return getattr(block_api_module, f'{block_pascal}Api')(self._sedaro_client)

    @cached_property
    def _block_group(self) -> str:
        '''The name of the Sedaro Block Group this type of Sedaro Block is stored in'''
        return self._branch_client._block_class_to_block_group_map[self._block_name]

        # Below can get block group if ever choose to not send blockClassToBlockGroupMap in response
        # PROPERTIES = 'properties'
        # REF = '$ref'
        # ANY_OF = 'anyOf'
        # ALL_OF = 'allOf'

        # block_group_type = None

        # # Traverse branch schema to figure out block group type, then traverse again to get matching block group
        # for k, v in self._branch_client.dataSchema['definitions'].items():
        #     # filter through all block group types
        #     if PROPERTIES in v and all(attr in v[PROPERTIES] for attr in ('name', 'collection', 'data')):
        #         # TODO: `if k.endswith('BG')` <-- evalutes to same as ^^^ if we always follow this convention for naming
        #         # block group classes. Would still like a safer way than either of these options though.
        #         blockClassOrClasses: Dict = v[PROPERTIES]['data']['additionalProperties']

        #         blockTypes = [blockClassOrClasses[REF]] if REF in blockClassOrClasses \
        #             else [v[REF] for v in blockClassOrClasses[ANY_OF]]

        #         if any(bT.endswith(self._block_name) for bT in blockTypes):
        #             block_group_type = k
        #             break

        # # check block group types (`bGT`) of all block groups to find which one matches `block_group_type`
        # for k, v in self._branch_client.dataSchema[PROPERTIES].items():
        #     if ALL_OF in v and any(bGT[REF].endswith(block_group_type) for bGT in v[ALL_OF]):
        #         return k

        # this shouldn't ever happen:
        # raise ValueError(
        #     f'Unable to find a block group containing the block name {self._block_name}')

    # TODO: better type hint
    def _get_create_or_update_block_model(self, create_or_update: Literal['create', 'update']) -> type:
        """Gets the model class to used to validate the data to create or update a Sedaro Block

        Args:
            create_or_update (Literal['create', 'update']): the action `'create'` or `'update'`

        Raises:
            ValueError: if you don't pass `'create'` or `'update'` for `create_or_update`

        Returns:
            type: the model used for validating # TODO: better type hint
        """
        create_or_update = create_or_update.lower()
        if create_or_update not in [CREATE, UPDATE]:
            raise ValueError(
                "The create_or_update arg must be either a string of either 'create' or 'update'.")

        block_snake, block_pascal = get_snake_and_pascal_case(self._block_name)

        crud_module_path = f'{BASE_PACKAGE_NAME}.model.{block_snake}'

        return getattr(
            import_module(f'{crud_module_path}_{create_or_update}'),
            f'{block_pascal}{create_or_update.capitalize()}'
        )

    def create(self, timeout: Union[int, Tuple] = None, **body) -> BlockClient:
        """Creates a Sedaro Block of the given type in the Sedaro database.

        Args:
            timeout (Union[int, Tuple], optional): the timeout used by the rest client. Defaults to `None`.
            **body (any): all remaining kwargs for the `body`

        Returns:
            BlockClient: a client to interact with the created Sedaro Block
        """
        res = getattr(self._block_openapi_instance, f'{CREATE}_{snake_case(self._block_name)}')(
            body=self._create_class(**body),
            path_params={'branchId': self._branch_client.id},
            timeout=timeout
        )
        block_id = self._branch_client._process_block_crud_response(res)

        return BlockClient(block_id, self)

    def get(self, id: Union[str, int]) -> BlockClient:
        """Gets a `BlockClient` of the desired type associated with the Sedaro Block of the given `id`.

        Args:
            id (Union[str, int]): `id` of the desired Sedaro Block

        Raises:
            TypeError: if the `id` is not an integer or an integer string
            KeyError: if no corresponding Block exists of the desired type

        Returns:
            BlockClient: a client to interact with the corresponding Sedaro Block
        """
        id = sanitize_and_enforce_id_in_branch(self._branch_client, id)

        # in addition to checks in ^^^ also make sure is the correct type for this block class client
        if self._branch_client._block_id_to_type_map[id] != self._block_name:
            raise KeyError(
                f'There is no "{self._block_name}" with id "{id}" in this Branch.')

        return BlockClient(id, self)

    def get_all_ids(self) -> List[str]:
        """Gets a `list` of `id`s corresponding to all Sedaro Blocks of the given type in this Branch. If there are no
        corresponding Blocks, returns an empty `list`.

        Returns:
            List[str]: list of `id`s
        """
        return [
            id for id in self._branch_client.data[self._block_group].keys()
            if self._branch_client._block_id_to_type_map[id] == self._block_name
        ]

    def get_all(self) -> List['BlockClient']:
        """Gets a `list` of all `BlockClient` instances corresponding to all Sedaro Blocks of the given type in this
        Branch. If there are no corresponding Blocks, returns an empty `list`.

        Returns:
            List['BlockClient']: a list of `BlockClient` instances corresponding to Sedaro Blocks in this Branch
        """
        return [BlockClient(id, self) for id in self.get_all_ids()]

    def get_first(self):
        """Returns a `BlockClient` associated with the least recently added (lowest `id`) Sedaro Block of the desired
        type.

        Raises:
            NoBlockFoundError: if no Blocks of the desired type exist in this Branch

        Returns:
            BlockClient: a client to interact with the corresponding Sedaro Block
        """
        all_ids = self.get_all_ids()
        if not len(all_ids):
            raise NoBlockFoundError(
                f'No "{self._block_name}" Blocks exist in this Branch.'
            )
        return BlockClient(sorted(all_ids, key=int)[0], self)

    def get_last(self):
        """Returns a `BlockClient` associated with the most recently added (highest `id`) Sedaro Block of the desired
        type.

        Raises:
            NoBlockFoundError: if no Blocks of the desired type exist in this Branch

        Returns:
            BlockClient: a client to interact with the corresponding Sedaro Block
        """
        all_ids = self.get_all_ids()
        if not len(all_ids):
            raise NoBlockFoundError(
                f'No "{self._block_name}" Blocks exist in this Branch.'
            )
        return BlockClient(sorted(all_ids, key=int)[-1], self)
