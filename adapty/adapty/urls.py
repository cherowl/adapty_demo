from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.views import DeviceViewSet, UserViewSet


router = routers.SimpleRouter()

router.register(r'users', UserViewSet)
router.register(r'devices', DeviceViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
