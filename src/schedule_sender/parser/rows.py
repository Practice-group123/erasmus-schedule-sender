"""Turn rows of one week block into Sessions.

Task 8. Every row with a non-empty Course becomes a Session.
No merging of double classes, no removing duplicates.
A bad row -> ParseIssue, the row is skipped, parsing continues.
"""

from schedule_sender.models import ParseResult, TableRef
from schedule_sender.parser.layout import WeekBlock


def parse_block(grid: list[list[str]], block: WeekBlock, ref: TableRef) -> ParseResult:
    raise NotImplementedError
