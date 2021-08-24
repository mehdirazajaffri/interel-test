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
    device_type = serializers.PrimaryKeyRelatedField(queryset=DeviceType.objects.all())
    reading = ReadingSerializer(many=True, read_only=True)
    class Meta:
        model = Device
        fields = ["id","name","device_type","reading"]
        extra_kwargs = {'reading': {'required': False}}


class DeviceReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ("id", "name",)


class ReadingDevicesSerializer(serializers.ModelSerializer):
    device = DeviceReadOnlySerializer(many=True, read_only=True)

    class Meta:
        model = Reading
        fields = ("updated_at", "temperature", "device")
