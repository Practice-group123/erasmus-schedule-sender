"""Task 3."""

from schedule_sender.models import RawSheet


def expand_merges(sheet: RawSheet) -> list[list[str]]:
    """Copy the value of every merged range's top-left cell into all its cells.

    Returns a new rectangular grid (all rows padded with "" to the same length).
    Does not modify the input.
    """
    raise NotImplementedError
