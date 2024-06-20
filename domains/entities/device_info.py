from __future__ import annotations

from dataclasses import dataclass

from .entity import Entity
from .device_id import DeviceId


@dataclass
class DeviceInfo(Entity):
    device_id: DeviceId
    app_version: str
    platform: str
    timezone: str

    @staticmethod
    def factory(device_id: DeviceId,
                app_version: str,
                platform: str,
                timezone: str
                ) -> DeviceInfo:

        device_info = DeviceInfo(
            device_id=device_id,
            app_version=app_version,
            platform=platform,
            timezone=timezone
        )

        return device_info
