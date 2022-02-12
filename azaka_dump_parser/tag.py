from __future__ import annotations

import gzip
import json
from enum import Enum
import typing as t

__all__ = ("Tag",)


class Cat(Enum):
    """
    An enum for the categories of tags.

    Attributes:
        CONT: The `content` category.
        ERO: The `sexual` category.
        TECH: The `technical` category.
    """
    CONT: str = "cont"
    ERO: str = "ero"
    TECH: str = "tech"


class Tag:
    """
    A class representing a `tag`.

    Attributes:
        id (int): The tag's ID.
        name (str): The tag's name.
        description (str): The tag's description.
        meta (bool): Whether the tag is a meta tag.
        searchable (bool): Whether the tag is searchable.
        applicable (bool): Whether this tag can be applied to VN entries.
        vns (int): The tag's VN count.
        cat (Cat): The tag's category.
        aliases (t.Iterable[str]): (Possibly empty) list of alternative names.
        parents (t.Iterable[int]): List of parent tags (empty for root tags). 
                The first element in this array points to the primary parent tag.
    """
    __slots__ = (
        "id",
        "name",
        "description",
        "meta",
        "searchable",
        "applicable",
        "vns",
        "cat",
        "aliases",
        "parents",
    )

    def __init__(self, data: t.Mapping[str, t.Any]) -> None:
        self.id: int = data["id"]
        self.name: str = data["name"]
        self.description: str = data["description"]
        self.meta: bool = data["meta"]
        self.searchable: bool = data["searchable"]
        self.applicable: bool = data["applicable"]
        self.vns: int = data["vns"]
        self.cat: Cat = Cat(data["cat"])
        self.aliases: t.Iterable[str] = data["aliases"]
        self.parents: t.Iterable[int] = data["parents"]

    @classmethod
    def from_dump(cls, file: gzip.GzipFile) -> t.Generator[Tag, None, None]:
        for data in json.load(file):
            yield cls(data)

    def __repr__(self) -> str:
        return f"<Tag id={self.id}>"
