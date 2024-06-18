from dataclasses import dataclass
from typing import Optional

from .shared import RootEntity, EntityId, EmailAddress
from .device import DeviceInfo


@dataclass
class Profile(RootEntity):
    profile_id: EntityId
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    email: Optional[EmailAddress]
    device_info: DeviceInfo
