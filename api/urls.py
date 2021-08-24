from django.urls import path, include
from rest_framework import routers

from . import views
from .views import DashboardView

router = routers.DefaultRouter()
router.register(r"devices", views.DeviceViewSet, basename="Device")
router.register(r"readings", views.ReadingViewSet, basename="Reading")
router.register(r"device-types", views.DeviceTypeViewSet, basename="DeviceTypes")

urlpatterns = [
    path("", include(router.urls)),
    path("dashboard/", DashboardView.as_view())
]
