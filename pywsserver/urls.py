from django.urls import path
from .views import DeviceCreateView, DeviceGetOne

urlpatterns = [
    path('api/devices', DeviceCreateView.as_view(), name='device-create'),
    path('api/devices/<str:id>', DeviceGetOne.as_view(), name='device-get'),
]