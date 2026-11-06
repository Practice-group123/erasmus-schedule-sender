import sys
import unittest
import warnings
from pathlib import Path


SOURCE_ROOT = Path(__file__).parents[1] / "src"
sys.path.insert(0, str(SOURCE_ROOT))

from schedule_sender.helpers.normalizers.normalize import (
    normalize_text,
    normalize_room,
    parse_day_cell,
    parse_time_range,
    resolve_year,
)
from schedule_sender.project_warnings.normalize_warnings import (
    NormalizeEmptyValueWarning,
    NormalizeInvalidAcademicYearWarning,
    NormalizeInvalidDayFormatWarning,
    NormalizeInvalidTimeFormatWarning,
)


class NormalizeTests(unittest.TestCase):
    def assert_warning(
        self, warning_type: type[Warning], expected_text: str, callback
    ) -> None:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            callback()

        self.assertEqual(len(caught), 1)
        self.assertIsInstance(caught[0].message, warning_type)
        self.assertEqual(str(caught[0].message), expected_text)

    def test_normalize_text_examples(self) -> None:
        self.assertEqual(normalize_text("  International   Private Law "), "internationalprivatelaw")
        self.assertEqual(normalize_text("Online"), "online")

    def test_normalize_text_warns_on_empty_input(self) -> None:
        self.assert_warning(
            NormalizeEmptyValueWarning,
            "Warning: empty variable in normalizer in normalize_text: raw is empty",
            lambda: self.assertEqual(normalize_text("   "), ""),
        )

    def test_parse_time_range_examples(self) -> None:
        self.assertEqual(parse_time_range("08:30-10:00"), "08:30-10:00")
        self.assertEqual(parse_time_range("8:30 - 10:00"), "8:30-10:00")
        self.assertEqual(parse_time_range("08.30-10.00"), "08:30-10:00")

    def test_parse_time_range_warns_on_empty_and_invalid_input(self) -> None:
        self.assert_warning(
            NormalizeEmptyValueWarning,
            "Warning: empty variable in normalizer in parse_time_range: raw is empty",
            lambda: self.assertEqual(parse_time_range(""), ""),
        )
        self.assert_warning(
            NormalizeInvalidTimeFormatWarning,
            "Warning: invalid time format in normalizer in parse_time_range: "
            "raw is not a valid time range: 08:30",
            lambda: self.assertEqual(parse_time_range("08:30"), ""),
        )

    def test_parse_day_cell_examples(self) -> None:
        self.assertEqual(parse_day_cell("26/10 Пнд (Mon)"), (26, 10, 0))
        self.assertEqual(parse_day_cell("26/10\nПнд\n(Mon)"), (26, 10, 0))

    def test_parse_day_cell_warns_on_empty_and_invalid_input(self) -> None:
        self.assert_warning(
            NormalizeEmptyValueWarning,
            "Warning: empty variable in normalizer in parse_day_cell: raw is empty",
            lambda: self.assertEqual(parse_day_cell(""), (0, 0, -1)),
        )
        self.assert_warning(
            NormalizeInvalidDayFormatWarning,
            "Warning: invalid day format in normalizer in parse_day_cell: "
            "raw is not a valid day cell: invalid",
            lambda: self.assertEqual(parse_day_cell("invalid"), (0, 0, -1)),
        )

    def test_resolve_year_examples(self) -> None:
        self.assertEqual(resolve_year(9, "2026/2027"), 2026)
        self.assertEqual(resolve_year(12, "2026/2027"), 2026)
        self.assertEqual(resolve_year(1, "2026/2027"), 2027)

    def test_resolve_year_warns_on_invalid_input(self) -> None:
        self.assert_warning(
            NormalizeEmptyValueWarning,
            "Warning: empty variable in normalizer in resolve_year: academic_year is empty",
            lambda: self.assertEqual(resolve_year(9, ""), 0),
        )
        self.assert_warning(
            NormalizeInvalidAcademicYearWarning,
            "Warning: invalid academic year in normalizer in resolve_year: month is not valid: 0",
            lambda: self.assertEqual(resolve_year(0, "2026/2027"), 0),
        )
        self.assert_warning(
            NormalizeInvalidAcademicYearWarning,
            "Warning: invalid academic year in normalizer in resolve_year: "
            "academic_year is not valid: 2026",
            lambda: self.assertEqual(resolve_year(9, "2026"), 0),
        )

    def test_normalize_room_examples(self) -> None:
        self.assertEqual(normalize_room("218"), "218")
        self.assertEqual(normalize_room(" Online "), "online")
        self.assertIsNone(normalize_room(""))

    def test_normalize_room_warns_on_empty_input(self) -> None:
        self.assert_warning(
            NormalizeEmptyValueWarning,
            "Warning: empty variable in normalizer in normalize_room: raw is empty",
            lambda: self.assertIsNone(normalize_room("")),
        )


if __name__ == "__main__":
    unittest.main()
