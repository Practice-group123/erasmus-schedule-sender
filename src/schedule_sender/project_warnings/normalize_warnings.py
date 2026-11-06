class NormalizeWarning(Warning):
    """A warning occurred in the normalizer.
    """

    def __init__(self, source: str, message: str) -> None:
        self.source = source
        self.message = message

    def __str__(self) -> str:
        return f"A warning occurred in the normalizer in {self.source}: {self.message}"

class NormalizeEmptyValueWarning(NormalizeWarning):
    """A warning occurred in the normalizer due to empty value.
    """

    def __init__(self, source: str, message: str) -> None:
        self.source = source
        self.message = message

    def __str__(self) -> str:
        return f"Warning: empty variable in normalizer in {self.source}: {self.message}"


class NormalizeInvalidTimeFormatWarning(NormalizeWarning):
    """A warning occurred in the normalizer due to invalid time format.
    """

    def __init__(self, source: str, message: str) -> None:
        self.source = source
        self.message = message

    def __str__(self) -> str:
        return f"Warning: invalid time format in normalizer in {self.source}: {self.message}"


class NormalizeInvalidDayFormatWarning(NormalizeWarning):
    """A warning occurred in the normalizer due to an invalid day cell.
    """

    def __init__(self, source: str, message: str) -> None:
        self.source = source
        self.message = message

    def __str__(self) -> str:
        return f"Warning: invalid day format in normalizer in {self.source}: {self.message}"
