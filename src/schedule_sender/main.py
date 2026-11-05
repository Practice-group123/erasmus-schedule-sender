import helpers.normalizers.normalize as normalize
def main() -> None:
    print(normalize.normalize_text("  International   Private Law "))
    print(normalize.parse_time_range("08:30-10:00"))
    print(normalize.parse_time_range("8.30 - 10.00"))
    print(normalize.parse_time_range(""))

    pass


if __name__ == "__main__":
    main()