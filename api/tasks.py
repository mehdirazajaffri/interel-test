from random import randint

from celery import shared_task

from api.models import Device, Reading


@shared_task
def read_temperature():
    count = Device.objects.count()
    d = Device.objects.all()[randint(0, count - 1)]
    r = Reading.objects.create(temperature=randint(60, 100))
    d.reading.add(r)
    d.save()
