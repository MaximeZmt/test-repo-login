# storage/memory.py
from typing import Any
from .base import Storage


class InMemoryStorage(Storage):
    """In-memory key-value storage implementation."""

    def __init__(self):
        self._store: dict[str, Any] = {}

    def put(self, key: str, value: Any) -> None:
        self._store[key] = value

    def get(self, key: str) -> Any:
        if key not in self._store:
            raise KeyError(f"Key '{key}' not found in storage")
        return self._store[key]

    def exist(self, key: str) -> bool:
        if key in self._store:
            return True
        return False