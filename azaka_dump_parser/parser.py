from __future__ import annotations

import gzip
import typing as t

from .vote import Vote
from .trait import Trait
from .tag import Tag

__all__ = ("Parser",)
TYPES = t.Union[Vote, Trait, Tag]


class Parser:
    """
    Main entry point for the library.
    """
    __slots__ = ("filename", "cls")

    def __init__(self, filename: str, cls: TYPES) -> None:
        """
        Parser constructor.

        args:
            filename: The name of file to parse.
            cls: The type of object to construct.
        
        Example:
            from azaka_dump_parser import Parser, Vote
            parser = Parser(filename="vote.json.gz", cls=Vote)
        
        It can also be used as a context manager:

        Example:
            from azaka_dump_parser import Parser, Vote

            with Parser(filename="vote.json.gz", cls=Vote) as parser:
                ...
        
        Info:
            Context manager handles file closing. If not using it then call the `close` method
            in the end.
        """
        self.filename = filename
        self.cls = cls

    @property
    def _file(self) -> gzip.GzipFile:
        """
        Tries opening the gzip file.

        Returns:
            The opened file.
        """
        return gzip.open(filename=self.filename, mode="rb")
    
    def __enter__(self) -> Parser:
        return self

    def __exit__(self, *_) -> None:
        self._file.close()

    def parse(self) -> t.Generator[TYPES, None, None]:
        """
        A generator that yields the parsed objects.

        Example:
            ```py
            from azaka_dump_parser import Parser, Vote

            with Parser(filename="vote.json.gz", cls=Vote) as parser:
                for vote in parser.parse():
                    print(vote)
            ```

        Danger:
            This generator will run until the file is exhausted.
            Depending on the file size it can take a while and cause a memory error.
        """
        yield from self.cls.from_dump(self._file)
