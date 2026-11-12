# Fake timetable fixture

`sample.xlsx` is a synthetic timetable. Its layout, formatting, and merged-cell
structure are based on the supplied timetable, but course names, rooms, and
program labels have been replaced with test data. No teacher names are included.

## Edge cases

Locations below refer to the timetable's visible week/day/time labels.

- **Online lesson:** W05, Tuesday, 10:10-11:40 (`online` in the Room column).
- **Double/extended slot block:** W05, Friday, 16:50-20:00. The original
  two-row merged time cells and parallel course rows are preserved.
- **Choice in Form:** W05, Friday, 11:50-15:00 (`выбор` in the Form column).
- **Empty day:** W05/W06, Thursday. Date and time grid remain, but all lesson
  details for that day are blank.

The fixture intentionally uses only `Test Subject A`, `Test Subject B`,
`Test Subject C`, rooms `101` and `102`, and program `Test Program`.
