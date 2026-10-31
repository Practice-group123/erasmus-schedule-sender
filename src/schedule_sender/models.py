"""Shared data types. Every module works with these, so change them only via PR
and tell the team.

Coordinates convention: rows and columns are 0-based everywhere in code.
Only ParseIssue.row is 1-based (it is shown to humans).
"""

from dataclasses import dataclass, field
from datetime import date, time

from schedule_sender.errors import ParseIssue


@dataclass(frozen=True)
class TableRef:
    """Which table to parse.

    id:   Google file ID, or a local path to .xlsx (tests, local runs)
    name: file name, e.g. "Право 3/ Law 3 (05-08 недели)"
    """

    id: str
    name: str


@dataclass(frozen=True)
class MergedRange:
    """A merged cell range. End is exclusive, like in the Google Sheets API.

    Example: Date cell A7:A14 -> MergedRange(6, 0, 14, 1)
    """

    start_row: int
    start_col: int
    end_row: int
    end_col: int


@dataclass
class RawSheet:
    """Raw content of the "Timetable" sheet, as read from the source.

    values: cell values as strings, "" for empty cells. Rows may differ in length.
    merges: merged ranges; values of merged cells are only in the top-left cell.
    """

    values: list[list[str]]
    merges: list[MergedRange] = field(default_factory=list)


@dataclass(frozen=True)
class Session:
    """One row of the timetable = one class in one time slot.

    Rows are not merged: a double class is two Sessions.
    """

    program: str            # "Право / Law"
    course: int             # 3
    week: str               # "W05"
    date: date
    start: time
    end: time
    subject: str            # "International Private Law", stored as written
    room: str | None        # "218", "online", None if empty
    source: str             # TableRef.name
    group: str | None = None  # meaning not confirmed yet


@dataclass
class ParseResult:
    sessions: list[Session] = field(default_factory=list)
    issues: list[ParseIssue] = field(default_factory=list)
