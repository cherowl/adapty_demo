from dataclasses import dataclass
from typing import Optional

from .entity import RootEntity
from .profile_id import ProfileId
from .email_address import EmailAddress


@dataclass
class Profile(RootEntity):
    profile_id: ProfileId
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    email: Optional[EmailAddress]
