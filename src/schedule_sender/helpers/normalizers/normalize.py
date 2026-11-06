from datetime import datetime, time

import warnings

from project_warnings.normalize_warnings import (
    NormalizeEmptyValueWarning,
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
    raise NotImplementedError


ACADEMIC_YEAR_START_MONTH = 9


def resolve_year(month: int, academic_year: str) -> int:
    """Pick the calendar year for a date without a year.

    academic_year comes from the sheet header, never hardcode it.
    "2026/2027": months from ACADEMIC_YEAR_START_MONTH to December -> 2026,
    January to the month before -> 2027. Warn on bad input.
    """
    raise NotImplementedError


def normalize_room(raw: str) -> str | None:
    """"218" -> "218", " Online " -> "online", "" -> None."""
    raise NotImplementedError
