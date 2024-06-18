from dataclasses import dataclass
from .shared import Entity, EntityId


@dataclass
class DeviceInfo(Entity):
    device_id: EntityId
    app_version: str
    platform: str
    timezone: str
