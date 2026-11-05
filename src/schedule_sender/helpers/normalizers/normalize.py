"""Pure helpers: raw cell text -> clean values. No I/O, easy to unit test.

Task 4.
"""

from datetime import datetime, time
import errors.normalize_errors as errors

def normalize_text(raw: str) -> str:
    """Trim and collapse whitespace. Case is kept.

    "  International   Private Law " -> "International Private Law"
    """

    non_space_raw = raw.replace(" ", "")
    if not non_space_raw:
        raise errors.NormalizeEmptyValueError("normalize_text", "raw is empty")
    
    lowered_raw = non_space_raw.lower()
    
    return lowered_raw


def parse_time_range(raw: str) -> tuple[time, time]:
    """"08:30-10:00" -> (time(8, 30), time(10, 0)).

    Also accept "8:30 - 10:00", "08.30-10.00". Raise ValueError on bad input.
    """
    non_space_raw = raw.replace(" ", "")
    if not non_space_raw:
        raise errors.NormalizeEmptyValueError("parse_time_range", "raw is empty")
    time_array = non_space_raw.replace(".", ":").split("-")
    if len(time_array) != 2:
        raise errors.NormalizeInvalidTimeFormatError("parse_time_range", f"raw is not a valid time range: {raw}")

    try:
        start_time = datetime.strptime(time_array[0], "%H:%M").time()
        end_time = datetime.strptime(time_array[1], "%H:%M").time()
    except ValueError:
        raise errors.NormalizeInvalidTimeFormatError("parse_time_range", f"raw is not a valid time range: {raw}")

    return (start_time, end_time)



def parse_day_cell(raw: str) -> tuple[int, int, int]:
    """"26/10 Пнд (Mon)" -> (26, 10, 0): day, month, weekday (Mon=0 ... Sun=6).

    The cell may contain line breaks. Raise ValueError on bad input.
    """
    raise NotImplementedError


ACADEMIC_YEAR_START_MONTH = 9


def resolve_year(month: int, academic_year: str) -> int:
    """Pick the calendar year for a date without a year.

    academic_year comes from the sheet header, never hardcode it.
    "2026/2027": months from ACADEMIC_YEAR_START_MONTH to December -> 2026,
    January to the month before -> 2027. Raise ValueError on bad input.
    """
    raise NotImplementedError


def normalize_room(raw: str) -> str | None:
    """"218" -> "218", " Online " -> "online", "" -> None."""
    raise NotImplementedError
