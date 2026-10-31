"""Where the raw table comes from. The parser does not know which source it uses.

Task 2.
"""

from typing import Protocol

from schedule_sender.models import RawSheet, TableRef

SHEET_NAME = "Timetable"


class GridSource(Protocol):
    def read(self, ref: TableRef) -> RawSheet:
        """Read the "Timetable" sheet. All values as strings, "" for empty cells."""
        ...


class XlsxSource:
    """Reads a downloaded .xlsx file (File -> Download -> .xlsx). ref.id is a path.

    Used in tests and local runs, no Google credentials needed.
    """

    def read(self, ref: TableRef) -> RawSheet:
        raise NotImplementedError


class SheetsSource:
    """Reads a table through the Google Sheets API. ref.id is a file ID.

    Stub until we get the service account.
    """

    def __init__(self, credentials_path: str) -> None:
        self.credentials_path = credentials_path

    def read(self, ref: TableRef) -> RawSheet:
        raise NotImplementedError
