"""Small checks shared by the domain classes."""


def check_id(value: int, label: str) -> int:
    """Makes sure an ID is a positive whole number. True/False don't count, even though Python treats them as 1/0."""
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{label} ID must be a positive whole number")
    return value


def check_text(value: str, label: str) -> str:
    """Makes sure a name or specialty isn't blank, and trims extra spaces."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} can't be empty")
    return value.strip()
