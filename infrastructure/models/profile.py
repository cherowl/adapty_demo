import uuid
from django.db import models

from .device_info import DeviceInfo


class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE = "m", "male"
        FEMALE = "f", "female"
        JUNIOR = "o", "other"

    profile_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(blank=True, max_length=25)
    last_name = models.CharField(blank=True, max_length=25)
    gender = models.CharField(choices=Gender, max_length=1)
    email = models.EmailField(max_length=254, unique=True)
    device_info = models.ForeignKey(DeviceInfo, on_delete=models.CASCADE)
