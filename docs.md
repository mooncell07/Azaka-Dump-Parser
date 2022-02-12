# `class` Parser

*Main entry point for the library.*

- args:
    - `filename`: The name of file to parse.
    - `cls`: The type of object to construct.

- Example:

```py
from azaka_dump_parser import Parser, Vote
parser = Parser(filename="vote.json.gz", cls=Vote)
```

It can also be used as a context manager:

```py
from azaka_dump_parser import Parser, Vote

with Parser(filename="vote.json.gz", cls=Vote) as parser:
    ...
```

- Info:

    Context manager handles file closing. If not using it then call the `close` method
    in the end.

## `.parse()`
A generator that yields the parsed objects.

- Returns:
    - Generator that yields the objects of type `cls`.

- Example:

```py
from azaka_dump_parser import Parser, Vote

with Parser(filename="vote.json.gz", cls=Vote) as parser:
    for vote in parser.parse():
        print(vote)
```

- Danger:

    This generator will run until the file is exhausted.
    Depending on the file size it can take a while and cause a memory error.


# `class` Tag

A class representing a `tag`.

- Attributes:

    - `id` (`int`): The tag's ID.
    - `name` (`str`): The tag's name.
    - `description` (`str`): The tag's description.
    - `meta` (`bool`): Whether the tag is a meta tag.`
    - `searchable` (`bool`): Whether the tag is searchable.
    - `applicable` (`bool`): Whether this tag can be applied to VN entries.
    - `vns` (`int`): The tag's VN count.
    - `cat` (`Cat`): The tag's category.
    - `aliases` (`t.Iterable[str]`): (Possibly empty) list of alternative names.
    - `parents` (`t.Iterable[int]`): List of parent - tags (empty for root tags). 
            The first element in this array points to the primary parent tag.

# `class` Trait

A class representing a `trait`.

- Attributes:

    - `id` (`int`): The trait's ID.
    - `name` (`str`): The trait's name.
    - `description` (`str`): The trait's description.
    - `meta` (`bool`): Whether the trait is a meta trait.
    - `searchable` (`bool`): Whether the trait is searchable.
    - `applicable` (`bool`): Whether this trait can be applied to character entries.
    - `chars` (`int`): Number of characters on which this trait and any child traits is used.
    - `aliases` (`t.Iterable[str]`): (Possibly empty) list of alternative names.
    - `parents` (`t.Iterable[int]`): List of parent traits (empty for root traits).
                                The first element in this array points to the primary parent trait.

# `class` Vote

A class representing a `vote`.

- Attributes:
    - `vn_id` (`int`): The VN's ID.
    - `user_id` (`int`): The user's ID.
    - `vote` (`int`): The vote's value multiplied by 10.
    - `date` (`str`): The date when the vote was added.


- Info:

    The vote files are not json.

# Examples

```py
from azaka_dump_parser import Parser, Tag

def test() -> Tag:
    parser = Parser("data/tags.gz", cls=Tag)
    return next(parser.parse())

print(test())
```

```py
from azaka_dump_parser import Parser, Vote

def test() -> Vote:
    with Parser("data/votes.gz", cls=Vote) as parser:
        votes = parser.parse()
    return next(votes)

print(test())
```

------