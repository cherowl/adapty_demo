from rest_framework import viewsets

from .models import DeviceInfo, Profile
from .serializers import DeviceInfoSerializer, ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing users.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class DeviceInfoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing devices.
    """
    queryset = DeviceInfo.objects.all()
    serializer_class = DeviceInfoSerializer
