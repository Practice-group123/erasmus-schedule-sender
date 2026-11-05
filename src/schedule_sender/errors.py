"""Errors and problems found while parsing schedule tables."""

from dataclasses import dataclass


class NormalizeError(Exception):
    """An error occurred in the normalizer.
    """

    def __init__(self, source: str, message: str) -> None:
        self.source = source
        self.message = message

    def __str__(self) -> str:
        return f"An error occurred in the normalizer in {self.source}: {self.message}"

class NormalizeEmptyValueError(NormalizeError):
    """An error occurred in the normalizer due to empty value.
    """

    def __init__(self, source: str, message: str) -> None:
        self.source = source
        self.message = message

    def __str__(self) -> str:
        return f"Error: empty variable in normalizer in {self.source}: {self.message}"

class ScheduleFormatError(Exception):
    """The table cannot be parsed at all (e.g. a required column is missing).

    Parsing of this table stops. Other tables are still parsed.
    """

    def __init__(self, source: str, message: str) -> None:
        self.source = source
        self.message = message
        super().__init__(f"{source}: {message}")


@dataclass(frozen=True)
class ParseIssue:
    """A problem with a single row. The row is skipped, parsing continues.

    row is 1-based, as shown in Google Sheets, so a human can find it.
    """

    source: str
    row: int
    message: str
