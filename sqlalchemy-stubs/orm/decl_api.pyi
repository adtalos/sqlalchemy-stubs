from typing import Any, TypeVar

T = TypeVar('T')

class DeclarativeMeta(type): ...

class registry(object):

    def mapped(self, cls: T) -> T: ...
    def generate_base(self) -> Any: ...
