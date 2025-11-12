# storage/base.py
from abc import ABC, abstractmethod
from typing import Any


class Storage(ABC):
    """Generic storage interface."""

    @abstractmethod
    def put(self, key: str, value: Any) -> None:
        """Store an object under a key."""
        pass

    @abstractmethod
    def exist(self, key: str) -> bool:
        """Is a key in Store."""
        pass

    @abstractmethod
    def get(self, key: str) -> Any:
        """Retrieve an object by key. Raises KeyError if not found."""
        pass
