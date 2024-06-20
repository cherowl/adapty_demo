from dataclasses import dataclass

from .value_object import EntityId


@dataclass(frozen=True)
class DeviceId(EntityId):
    pass
