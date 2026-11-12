"""Where the raw table comes from. The parser does not know which source it uses.

Task 2.
"""

from datetime import date, datetime, time
from typing import Protocol

from openpyxl import load_workbook

from schedule_sender.models.models import RawSheet, TableRef, MergedRange


SHEET_NAME = "Timetable"


class GridSource(Protocol):
    def read(self, ref: TableRef) -> RawSheet:
        """Read the Timetable sheet. All values as strings."""
        ...


class XlsxSource:
    """Reads a local XLSX file without Google credentials."""

    def read(self, ref: TableRef) -> RawSheet:
        workbook = load_workbook(ref.id, data_only=True)

        try:
            if SHEET_NAME not in workbook.sheetnames:
                raise ValueError(
                    f"Sheet '{SHEET_NAME}' not found in file: {ref.id}"
                )

            worksheet = workbook[SHEET_NAME]

            def cell_to_string(value) -> str:
                if value is None:
                    return ""

                if isinstance(value, datetime):
                    return value.isoformat(sep=" ")

                if isinstance(value, date):
                    return value.isoformat()

                if isinstance(value, time):
                    return value.strftime("%H:%M")

                return str(value)

            # Read all cells as strings
            values = [
                [cell_to_string(value) for value in row]
                for row in worksheet.iter_rows(values_only=True)
            ]

            # Read merged ranges using 0-based coordinates
            merges = [
                MergedRange(
                    start_row=merged.min_row - 1,
                    start_col=merged.min_col - 1,
                    end_row=merged.max_row,
                    end_col=merged.max_col,
                )
                for merged in worksheet.merged_cells.ranges
            ]

            return RawSheet(
                values=values,
                merges=merges,
            )

        finally:
            workbook.close()


class SheetsSource:
    """Google Sheets source. Stub until service account is available."""

    def __init__(self, credentials_path: str) -> None:
        self.credentials_path = credentials_path

    def read(self, ref: TableRef) -> RawSheet:
        raise NotImplementedError
