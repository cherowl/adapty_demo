import pytz

from rest_framework import serializers, validators
from infrastructure.models import DeviceInfo, Profile

import logging

logger = logging.getLogger(__name__)


class DeviceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInfo
        fields = ['device_id', 'app_version', 'platform', 'timezone']

    def validate(self, data):
        if data['timezone'] not in pytz.all_timezones:
            raise serializers.ValidationError({"timezone": "Timezone is inncorrect"})
        return data


class ProfileSerializer(serializers.ModelSerializer):
    device_info = DeviceInfoSerializer(required=True)

    class Meta:
        model = Profile
        fields = ['profile_id', 'first_name', 'last_name', 'gender', 'email', 'device_info']

        validators = [
            validators.UniqueTogetherValidator(
                queryset=Profile.objects.all(),
                fields=['platform_id', 'device_id']
            )
        ]