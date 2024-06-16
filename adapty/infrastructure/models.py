import uuid
from django.db import models


class Device(models.Model):
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


class User(models.Model):
    class Gender(models.TextChoices):
        MALE = "m", "male"
        FEMALE = "f", "female"
        JUNIOR = "o", "other"

    profile_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(blank=True, max_length=25)
    last_name = models.CharField(blank=True, max_length=25)
    gender = models.CharField(choices=Gender, max_length=1)
    email = models.EmailField(max_length=254, unique=True)
    device_info = models.ForeignKey(Device, on_delete=models.CASCADE)