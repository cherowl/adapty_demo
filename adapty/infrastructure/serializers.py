import pytz

from rest_framework import serializers, validators
from infrastructure.models import Device, User

import logging

logger = logging.getLogger(__name__)


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['device_id', 'app_version', 'platform', 'timezone']

    def validate(self, data):
        if data['timezone'] not in pytz.all_timezones:
            raise serializers.ValidationError({"timezone": "Timezone is inncorrect"})
        return data


class UserSerializer(serializers.ModelSerializer):
    device_info = DeviceSerializer(required=True)

    class Meta:
        model = User
        fields = ['profile_id', 'first_name', 'last_name', 'gender', 'email', 'device_info']

        validators = [
            validators.UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['platform_id', 'device_id']
            )
        ]