class NormalizeError(Exception):
    """An error occurred in the normalizer.
    """

    def __init__(self, source: str, message: str) -> None:
        self.source = source
        self.message = message

    def __str__(self) -> str:
        return f"An error occurred in the normalizer in {self.source}: {self.message}"

class NormalizeEmptyValueError(NormalizeError):
    """An error occurred in the normalizer due to empty value.
    """

    def __init__(self, source: str, message: str) -> None:
        self.source = source
        self.message = message

    def __str__(self) -> str:
        return f"Error: empty variable in normalizer in {self.source}: {self.message}"
class NormalizeInvalidTimeFormatError(NormalizeError):
    """An error occurred in the normalizer due to invalid time format.
    """

    def __init__(self, source: str, message: str) -> None:
        self.source = source
        self.message = message

    def __str__(self) -> str:
        return f"Error: invalid time format in normalizer in {self.source}: {self.message}"