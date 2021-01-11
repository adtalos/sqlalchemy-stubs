import sys

from typing import Any, Iterable, List, Mapping, Optional, Iterator, Union, AbstractSet, Tuple
from ..sql.schema import Column

if sys.version_info >= (3, 0):
    _RowItems = AbstractSet[Tuple[str, Any]]
else:
    _RowItems = List[Tuple[str, Any]]

def rowproxy_reconstructor(cls, state): ...

class BaseRowProxy(Mapping[str, Any]):
    def __init__(self, parent, row, processors, keymap) -> None: ...
    def __reduce__(self) -> Any: ...
    def values(self) -> List[Any]: ...
    def __iter__(self) -> Iterable[Any]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: Union[str, int, Column]) -> Any: ...
    def __getattr__(self, name)-> Any: ...

class RowProxy(BaseRowProxy):
    def __contains__(self, key) -> bool: ...
    __hash__: Any = ...
    def __lt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def has_key(self, key) -> bool: ...
    def items(self) -> _RowItems: ...
    def keys(self) -> List[Union[str, int]]: ...
    def iterkeys(self) -> Iterable[Union[str, int]]: ...
    def itervalues(self) -> Iterable[Any]: ...

class ResultMetaData(object):
    case_sensitive: Any = ...
    matched_on_name: bool = ...
    def __init__(self, parent, cursor_description) -> None: ...

class ResultProxy:
    out_parameters: Any = ...
    closed: bool = ...
    context: Any = ...
    dialect: Any = ...
    cursor: Any = ...
    connection: Any = ...
    def __init__(self, context) -> None: ...
    def keys(self): ...
    @property
    def rowcount(self) -> int: ...
    @property
    def lastrowid(self): ...
    @property
    def returns_rows(self): ...
    @property
    def is_insert(self): ...
    def close(self) -> None: ...
    def __iter__(self) -> Iterator[RowProxy]: ...
    def __next__(self) -> RowProxy: ...
    def next(self) -> RowProxy: ...
    @property
    def inserted_primary_key(self): ...
    def last_updated_params(self): ...
    def last_inserted_params(self): ...
    @property
    def returned_defaults(self): ...
    def lastrow_has_defaults(self): ...
    def postfetch_cols(self): ...
    def prefetch_cols(self): ...
    def supports_sane_rowcount(self): ...
    def supports_sane_multi_rowcount(self): ...
    def process_rows(self, rows): ...
    def fetchall(self) -> List[RowProxy]: ...
    def fetchmany(self, size: Optional[int] = ...) -> List[RowProxy]: ...
    def fetchone(self) -> Optional[RowProxy]: ...
    def first(self) -> Optional[RowProxy]: ...
    # Note: The return type `Any` should be a DB API 2 value type once defined
    # TODO: See typeshed/#1037
    def scalar(self) -> Any: ...

class BufferedRowResultProxy(ResultProxy):
    size_growth: Any = ...

class FullyBufferedResultProxy(ResultProxy): ...

class BufferedColumnRow(RowProxy):
    def __init__(self, parent, row, processors, keymap) -> None: ...

class BufferedColumnResultProxy(ResultProxy):
    def fetchall(self): ...
    def fetchmany(self, size: Optional[Any] = ...): ...
