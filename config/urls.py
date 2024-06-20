from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from infrastructure.views import DeviceInfoViewSet, ProfileViewSet


router = routers.SimpleRouter()

router.register(r'profiles', ProfileViewSet)
router.register(r'devices_info', DeviceInfoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
