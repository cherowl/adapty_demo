import re, uuid
from dataclasses import dataclass
from email.utils import parseaddr


@dataclass(frozen=True)
class EntityId:
    id: uuid.UUID


@dataclass(frozen=True)
class EmailAddress:
    value: str

    def __post_init__(self) -> None:
        email_address = self.value

        regex_result = re.search(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",
            email_address,
        )
        if not regex_result:
            raise ValueError("Incorrect email address!")

    def __str__(self) -> str:
        return self.value


@dataclass
class Entity:
    """A base class for all entities"""
    id: EntityId

@dataclass
class RootEntity(Entity):
    pass