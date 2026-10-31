"""Find week blocks on the sheet.

The sheet has several blocks side by side (A-F, H-M) and below each other
(rows 1-60, 62-...). Each block has a header row:
    Date | Time | Room | Course | Teacher | Form
Above it: academic year, "Курс 3", program, week label "W05".

Task 7.
"""

from dataclasses import dataclass

from schedule_sender.models import TableRef

REQUIRED_COLUMNS = ("Date", "Time", "Room", "Course")
OPTIONAL_COLUMNS = ("Form",)


@dataclass(frozen=True)
class WeekBlock:
    header_row: int            # row of "Date | Time | ...", 0-based
    first_row: int             # first data row, 0-based
    last_row: int              # last data row, inclusive
    columns: dict[str, int]    # "Date" -> column index, ... (optional ones may be absent)
    week: str                  # "W05"
    academic_year: str         # "2026/2027"
    course: int
    program: str


def find_week_blocks(grid: list[list[str]], ref: TableRef) -> list[WeekBlock]:
    """Find all week blocks. grid is already expanded (merged cells filled).

    Raise ScheduleFormatError(ref.name, ...) if no blocks are found,
    a required column is missing in a block, or the academic year, course
    or week label is not found in the header. Never fall back to defaults
    (e.g. the current year).
    """
    raise NotImplementedError
