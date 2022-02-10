from __future__ import annotations

import gzip
import typing as t

from .vote import Vote

__all__ = ("Parser",)


class Parser:
    __slots__ = ("filename",)

    def __init__(self, filename: str) -> None:
        self.filename = filename

    @property
    def _file(self) -> gzip.GzipFile:
        return gzip.open(filename=self.filename, mode="rb")

    def read_first(self) -> Vote:
        return Vote.from_dump(self._file.readline())

    def read_all(self) -> t.Generator[Vote, None, None]:
        yield from map(Vote.from_dump, self._file)
