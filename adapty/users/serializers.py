from rest_framework import serializers
from users.models import Device, User


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['device_id', 'app_version', 'platform', 'timezone']


class UserSerializer(serializers.ModelSerializer):
    device_info = DeviceSerializer(required=True)

    class Meta:
        model = User
        fields = ['profile_id', 'first_name', 'last_name', 'gender', 'email', 'device_info']