from dataclasses import dataclass


@dataclass(frozen=True)
class ValueObject:
    """
    A base class for all value objects
    to measure quantities or describe characteristics.

    Comparable by value.
    """

    value: str

    def __str__(self):
        return str(self.value)
