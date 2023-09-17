# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorView(APIView):
    def post(self, request):
        data = request.data
        sensor = Sensor(name=data['name'], description=data['description'])
        sensor.save()
        return Response({'status': 'OK'})

    def get(self, request):
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        return Response(ser.data)


class SensorOneView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        sensor.description = request.data['description']
        sensor.save()
        return Response({'status': 'OK'})


class MeasurementsView(APIView):
    def post(self, request):
        data = request.data
        measurement = Measurement(sensor_id=data['sensor'], temperature=data['temperature'])
        measurement.save()
        return Response({'status': 'OK'})


class SensorDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
