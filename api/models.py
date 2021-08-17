import json
import operator
from datetime import timedelta, datetime

from django.core import serializers
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from api.redis import publish


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Device(BaseModel):
    id = models.CharField(primary_key=True, blank=False, null=False, max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField(
        null=True, blank=True, help_text="Device Description")
    device_type = models.ForeignKey(
        "DeviceType",
        related_name="devices",
        on_delete=models.PROTECT,
        null=True
    )
    reading = models.ManyToManyField("Reading", related_name="device", blank=True)

    @classmethod
    def get_stats(cls, date_from, date_to):
        device_readings = cls.objects.filter(reading__updated_at__gte=date_from,
                                             reading__updated_at__lte=date_to).distinct()
        temp = {}
        for i in device_readings:
            temp[i.name] = (i.reading.count())

        return {
            "maximum_readings": max(temp.items(), key=operator.itemgetter(1)) or None,
            "minimum_readings": min(temp.items(), key=operator.itemgetter(1)) or None
        }

    def __str__(self) -> str:
        return "{} -> {}".format(self.id, self.device_type.type)


class DeviceType(BaseModel):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class Reading(BaseModel):
    temperature = models.IntegerField(default=0, help_text="Temperature")
    data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return str(self.temperature)


@receiver(post_save, sender=Device)
def publish_device_info(sender, instance, created, **kwargs):
    if created:
        serialized_obj = serializers.serialize('json', [instance, ])
        print(serialized_obj)
        publish("devices", serialized_obj)
        # publish("stats", json.dumps(sender.get_stats(datetime.utcnow().date() - timedelta(days=7),
        #                                              datetime.utcnow().date() + timedelta(days=1))))
