from dataclasses import dataclass

from .value_object import EntityId


@dataclass(frozen=True)
class Entity:
    """A base class for all entities"""
    id: EntityId


@dataclass(frozen=True)
class RootEntity(Entity):
    """This is root entity of some Aggregate group"""
    pass
