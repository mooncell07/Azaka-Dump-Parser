from __future__ import annotations

import gzip
import typing as t

__all__ = ("Vote",)


class Vote:
    """
    A class representing a `vote`.

    Attributes:
        vn_id (int): The VN's ID.
        user_id (int): The user's ID.
        vote (int): The vote's value multiplied by 10.
        date (str): The date when the vote was added.

    Info:
        The vote files are not json.
    """

    __slots__ = ("vn_id", "user_id", "vote", "date")

    def __init__(self, vn_id: int, user_id: int, vote: int, date: str) -> None:
        self.vn_id = vn_id
        self.user_id = user_id
        self.vote = vote
        self.date = date

    @classmethod
    def from_dump(cls, file: gzip.GzipFile) -> t.Generator[Vote, None, None]:
        for data in file.readlines():
            parameters: list = data.decode().split()
            parameters[:-1] = [int(x) for x in parameters[:-1]]
            yield cls(*parameters)


    def __repr__(self) -> str:
        return f"<Vote vn_id={self.vn_id}>"
