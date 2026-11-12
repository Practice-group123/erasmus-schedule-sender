"""Task 3."""


"""Expand merged cells into a rectangular grid."""

from schedule_sender.models.models import RawSheet


def expand_merges(sheet: RawSheet) -> list[list[str]]:
    """
    Copy the top-left cell value into every cell of each merged range.

    Returns a new rectangular grid and does not modify the input.
    """

    # Create a copy of the original values
    result = [row.copy() for row in sheet.values]

    # Calculate required table dimensions
    max_rows = max(
        len(result),
        max((merge.end_row for merge in sheet.merges), default=0)
    )

    max_cols = max(
        max((len(row) for row in result), default=0),
        max((merge.end_col for merge in sheet.merges), default=0)
    )

    # Add missing rows
    while len(result) < max_rows:
        result.append([])

    # Make all rows the same length
    for row in result:
        row.extend([""] * (max_cols - len(row)))

    # Expand merged ranges
    for merge in sheet.merges:
        value = result[merge.start_row][merge.start_col]

        for row in range(merge.start_row, merge.end_row):
            for col in range(merge.start_col, merge.end_col):
                result[row][col] = value

    return result
