from __future__ import annotations

import gzip
import json
import typing as t

__all__ = ("Trait",)


class Trait:
    """
    A class representing a `trait`.

    Attributes:
        id (int): The trait's ID.
        name (str): The trait's name.
        description (str): The trait's description.
        meta (bool): Whether the trait is a meta trait.
        searchable (bool): Whether the trait is searchable.
        applicable (bool): Whether this trait can be applied to character entries.
        chars (int): Number of characters on which this trait and any child traits is used.
        aliases (t.Iterable[str]): (Possibly empty) list of alternative names.
        parents (t.Iterable[int]): List of parent traits (empty for root traits).
                                    The first element in this array points to the primary parent trait.
    """

    __slots__ = (
        "id",
        "name",
        "description",
        "meta",
        "searchable",
        "applicable",
        "chars",
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
        self.chars: int = data["chars"]
        self.aliases: t.Iterable[str] = data["aliases"]
        self.parents: t.Iterable[int] = data["parents"]

    @classmethod
    def from_dump(cls, file: gzip.GzipFile) -> t.Generator[Trait, None, None]:
        for data in json.load(file):
            yield cls(data)

    def __repr__(self) -> str:
        return f"<Trait id={self.id}>"
