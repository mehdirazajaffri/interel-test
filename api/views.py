# Create your views here.
import datetime
import logging
import operator
from datetime import datetime, timedelta

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.response import Response

from api.models import Device, Reading
from api.serializers import DeviceSerializer, ReadingDevicesSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by("-updated_at")
    serializer_class = DeviceSerializer


class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all().order_by("-updated_at")
    serializer_class = ReadingDevicesSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = {
        'updated_at': ['gte', 'lte'],
    }


class DashboardView(generics.GenericAPIView):
    queryset = Device.objects.all()

    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = {
    #     'updated_at': ['gte', 'lte'],
    # }

    def get(self, request):
        try:
            date_from = request.query_params.get('from', datetime.utcnow().date() - timedelta(days=7))
            date_to = request.query_params.get('to', datetime.utcnow().date() + timedelta(days=1))

            temp = {}

            device_readings = self.queryset.filter(reading__updated_at__gte=date_from,
                                                   reading__updated_at__lte=date_to).distinct()

            for i in device_readings:
                temp[i.name] = (i.reading.count())

            return Response([{
                "maximum_readings": max(temp.items(), key=operator.itemgetter(1)) or None,
                "minimum_readings": min(temp.items(), key=operator.itemgetter(1)) or None
            }])
        except Exception as e:
            logging.error(e)
            return Response({}, 400)
