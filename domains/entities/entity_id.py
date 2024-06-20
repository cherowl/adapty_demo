from dataclasses import dataclass
from uuid import UUID

from .value_object import ValueObject
from ..errors.value_object import UUIDValueError

UUID_VERSION = 4


@dataclass(frozen=True)
class EntityId(ValueObject):
    value: UUID

    def __post_init__(self) -> None:
        try:
            UUID(str(self.value), version=UUID_VERSION)
        except ValueError:
            raise UUIDValueError(self.value)