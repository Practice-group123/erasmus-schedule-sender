from datetime import datetime, time
import re

import warnings

from project_warnings.normalize_warnings import (
    NormalizeEmptyValueWarning,
    NormalizeInvalidAcademicYearWarning,
    NormalizeInvalidDayFormatWarning,
    NormalizeInvalidTimeFormatWarning,
)

def normalize_text(raw: str) -> str:
    """Trim and collapse whitespace. Case is kept.

    "  International   Private Law " -> "International Private Law"
    """

    non_space_raw = raw.replace(" ", "")
    if not non_space_raw:
        warnings.warn(
            NormalizeEmptyValueWarning("normalize_text", "raw is empty"),
            stacklevel=2,
        )
        return ""
    
    lowered_raw = non_space_raw.lower()
    
    return lowered_raw


def parse_time_range(raw: str) -> str:
    """" 08:3 0 - 10:00 " -> "08:00-10:00".

    Also accept "8:30 - 10:00", "08.30-10.00". Warn and return None on bad input.
    """
    non_space_raw = raw.replace(" ", "")
    if not non_space_raw:
        warnings.warn(
            NormalizeEmptyValueWarning("parse_time_range", "raw is empty"),
            stacklevel=2,
        )
        return ""
    time_array = non_space_raw.replace(".", ":").split("-")
    if len(time_array) != 2:
        warnings.warn(
            NormalizeInvalidTimeFormatWarning(
                "parse_time_range", f"raw is not a valid time range: {raw}"
            ),
            stacklevel=2,
        )
        return ""
    return f"{time_array[0]}-{time_array[1]}"



def parse_day_cell(raw: str) -> tuple[int, int, int]:
    """"26/10 Пнд (Mon)" -> (26, 10, 0): day, month, weekday (Mon=0 ... Sun=6).

    The cell may contain line breaks. Warn on bad input.
    """
    if not raw or not raw.strip():
        warnings.warn(
            NormalizeEmptyValueWarning("parse_day_cell", "raw is empty"),
            stacklevel=2,
        )
        return (0, 0, -1)

    compact_raw = re.sub(r"\s+", " ", raw).strip()
    match = re.fullmatch(
        r"(?P<day>\d{1,2})\s*/\s*(?P<month>\d{1,2})\s+"
        r"(?P<weekday>[^\s()]+)(?:\s+\((?P<english_weekday>[^()]*)\))?",
        compact_raw,
    )
    weekday_names = {
        "пнд": 0,
        "пн": 0,
        "mon": 0,
        "втр": 1,
        "вт": 1,
        "tue": 1,
        "ср": 2,
        "срд": 2,
        "wed": 2,
        "чтв": 3,
        "чт": 3,
        "thu": 3,
        "птн": 4,
        "пт": 4,
        "fri": 4,
        "сб": 5,
        "sat": 5,
        "вск": 6,
        "вс": 6,
        "sun": 6,
    }

    if match is None:
        warnings.warn(
            NormalizeInvalidDayFormatWarning(
                "parse_day_cell", f"raw is not a valid day cell: {raw}"
            ),
            stacklevel=2,
        )
        return (0, 0, -1)

    day = int(match.group("day"))
    month = int(match.group("month"))
    weekday = weekday_names.get(match.group("weekday").lower())
    english_weekday = match.group("english_weekday")
    if weekday is None and english_weekday is not None:
        weekday = weekday_names.get(english_weekday.strip().lower())

    try:
        datetime(2000, month, day)
    except ValueError:
        weekday = None

    if weekday is None:
        warnings.warn(
            NormalizeInvalidDayFormatWarning(
                "parse_day_cell", f"raw is not a valid day cell: {raw}"
            ),
            stacklevel=2,
        )
        return (0, 0, -1)

    return (day, month, weekday)


ACADEMIC_YEAR_START_MONTH = 9


def resolve_year(month: int, academic_year: str) -> int:
    """Pick the calendar year for a date without a year.

    academic_year comes from the sheet header, never hardcode it.
    "2026/2027": months from ACADEMIC_YEAR_START_MONTH to December -> 2026,
    January to the month before -> 2027. Warn on bad input.
    """
    if not academic_year or not academic_year.strip():
        warnings.warn(
            NormalizeEmptyValueWarning("resolve_year", "academic_year is empty"),
            stacklevel=2,
        )
        return 0

    if not isinstance(month, int) or not 1 <= month <= 12:
        warnings.warn(
            NormalizeInvalidAcademicYearWarning(
                "resolve_year", f"month is not valid: {month}"
            ),
            stacklevel=2,
        )
        return 0

    academic_year_match = re.fullmatch(
        r"(\d{4})\s*/\s*(\d{4})", academic_year.strip()
    )
    if academic_year_match is None:
        warnings.warn(
            NormalizeInvalidAcademicYearWarning(
                "resolve_year",
                f"academic_year is not valid: {academic_year}",
            ),
            stacklevel=2,
        )
        return 0

    start_year = int(academic_year_match.group(1))
    end_year = int(academic_year_match.group(2))
    if end_year != start_year + 1:
        warnings.warn(
            NormalizeInvalidAcademicYearWarning(
                "resolve_year",
                f"academic_year does not contain consecutive years: {academic_year}",
            ),
            stacklevel=2,
        )
        return 0

    if month >= ACADEMIC_YEAR_START_MONTH:
        return start_year
    return end_year


def normalize_room(raw: str) -> str | None:
    """"218" -> "218", " Online " -> "online", "" -> None."""
    if not raw or not raw.strip():
        warnings.warn(
            NormalizeEmptyValueWarning("normalize_room", "raw is empty"),
            stacklevel=2,
        )
        return None

    return re.sub(r"\s+", " ", raw).strip().lower()
