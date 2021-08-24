# Create your views here.
import datetime
import logging
from datetime import datetime, timedelta

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.response import Response

from api.models import Device, DeviceType, Reading
from api.serializers import DeviceSerializer, DeviceTypeSerializer, ReadingDevicesSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by("-updated_at")
    serializer_class = DeviceSerializer


class DeviceTypeViewSet(viewsets.ModelViewSet):
    queryset = DeviceType.objects.all().order_by("-updated_at")
    serializer_class = DeviceTypeSerializer

class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all().order_by("-updated_at")
    serializer_class = ReadingDevicesSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = {
        'updated_at': ['gte', 'lte'],
    }


class DashboardView(generics.GenericAPIView):
    queryset = Device.objects.all()

    def get(self, request):
        try:
            date_from = request.query_params.get('from', datetime.utcnow().date() - timedelta(days=7))
            date_to = request.query_params.get('to', datetime.utcnow().date() + timedelta(days=1))

            return Response(self.queryset.model.get_stats(date_from, date_to))
        except Exception as e:
            logging.error(e)
            return Response({}, 400)
