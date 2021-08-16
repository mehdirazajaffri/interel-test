from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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
        print(instance)
        # send_email.delay(
        #     {
        #         "to": "gc@oj-lifestyle.com,mr@berkeley-assets.com",
        #         "subject": "{} requested for a benefit".format(instance.partner.name),
        #         "html_body": render_to_string('benefit_add_request.html', context)
        #     }
        # )
