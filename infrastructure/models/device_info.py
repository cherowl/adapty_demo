import uuid
from django.db import models


class DeviceInfo(models.Model):
    class Platform(models.TextChoices):
        IOS = "iOS"
        MAC = "macOS"
        IPAD = "iPadOS"
        VISION = "visionOS"
        ANDROID = "Android"

    device_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    app_version = models.CharField(max_length=10)
    platform = models.CharField(choices=Platform, max_length=25)
    timezone = models.CharField(max_length=100)
