from django.urls import path
from .views import SensorView, SensorOneView, MeasurementView


urlpatterns = [
    path('sensors/', SensorView.as_view(), name='sensor'),
    path('sensors/<pk>/', SensorOneView.as_view(), name='sensor_one'),
    path('measurements/', MeasurementView.as_view(), name='measure'),
]
