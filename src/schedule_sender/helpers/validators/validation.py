"""Checks for a parsed Session. Return problems, never raise.

Task 5. Do NOT check for duplicates: the same subject in the same slot
can be different groups, this is not an error for the parser.
"""

from datetime import date

from schedule_sender.errors import ParseIssue
from schedule_sender.models import Session


def validate_session(
    session: Session,
    row: int,
    weekday_in_cell: int,
    semester_start: date | None = None,
    semester_end: date | None = None,
) -> list[ParseIssue]:
    """Return a list of problems, empty if the session is fine.

    Checks:
    - subject is not empty
    - start is earlier than end
    - session.date.weekday() == weekday_in_cell ("Пнд" in the cell is really a Monday)
    - date is inside the semester, if semester dates are given

    row is 1-based (for ParseIssue).
    """
    raise NotImplementedError
