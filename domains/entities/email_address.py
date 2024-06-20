import re
from dataclasses import dataclass

from .value_object import ValueObject
from ..errors.value_object import EmailAddressError


@dataclass(frozen=True)
class EmailAddress(ValueObject):
    value: str

    def __post_init__(self) -> None:
        email_address = self.value

        regex_result = re.search(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",
            email_address,
        )

        if not regex_result:
            raise EmailAddressError(self.value)
