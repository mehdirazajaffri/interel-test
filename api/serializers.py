from rest_framework import serializers

from .models import Device, Reading, DeviceType


class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceType
        fields = "__all__"


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):
    reading = ReadingSerializer(many=True)
    device_type = DeviceTypeSerializer()

    class Meta:
        model = Device
        fields = "__all__"


class DeviceReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ("id", "name",)


class ReadingDevicesSerializer(serializers.ModelSerializer):
    device = DeviceReadOnlySerializer(many=True, read_only=True)

    class Meta:
        model = Reading
        fields = ("updated_at", "temperature", "device")
