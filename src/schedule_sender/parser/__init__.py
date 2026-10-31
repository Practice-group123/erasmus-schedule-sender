"""Bachelor schedule parser.

Pipeline for one table:
    source.read(ref) -> RawSheet
    expand_merges(sheet) -> grid
    find_week_blocks(grid, ref) -> list[WeekBlock]
    parse_block(grid, block, ref) -> ParseResult   (for every block)

Task 9.
"""

from schedule_sender.models import ParseResult, TableRef
from schedule_sender.parser.sources import GridSource


def parse_table(ref: TableRef, source: GridSource) -> ParseResult:
    """Parse one table and merge results of all week blocks.

    Raises ScheduleFormatError if the table layout is broken.
    """
    raise NotImplementedError
