from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Device, User
from .serializers import DeviceSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class DeviceViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing devices.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAdminUser]
