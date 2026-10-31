"""Which tables to parse.

Task 6. Temporary: the list comes from config. Real search in Drive folders
(including subfolders like "1 курс / 1st year") is a separate task later.
"""

from dataclasses import dataclass
from typing import Protocol

from schedule_sender.models import TableRef


class TableLocator(Protocol):
    def list_tables(self) -> list[TableRef]: ...


class StaticLocator:
    """Returns a fixed list of tables (paths or IDs from config)."""

    def __init__(self, tables: list[TableRef]) -> None:
        self.tables = tables

    def list_tables(self) -> list[TableRef]:
        raise NotImplementedError


@dataclass(frozen=True)
class TableName:
    program: str   # "Право / Law"
    course: int    # 3
    weeks: str     # "05-08"


def parse_table_name(name: str) -> TableName:
    """"Право 3/ Law 3 (05-08 недели)" -> TableName("Право / Law", 3, "05-08").

    "Informatics 3 (05-08 недели)" -> TableName("Informatics", 3, "05-08").
    Raise ValueError if the name does not match.
    """
    raise NotImplementedError
