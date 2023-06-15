from rest_framework.generics import (ListCreateAPIView,
                                    RetrieveUpdateAPIView,
                                    CreateAPIView)
from .models import Sensor, Measurement
from .serializers import (SensorSerializer,
                          SensorDetailSerializer,
                          MeasurementSerializer,
                          MeasurementCreateSerializer)


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorOneView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer
