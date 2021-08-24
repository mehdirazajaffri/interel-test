from django.contrib import admin

# Register your models here.
from api.models import Device, DeviceType, Reading

admin.site.register(DeviceType)
admin.site.register(Reading)


admin.site.site_title = "Iot Devices"
admin.site.site_header = "Iot Devices"
admin.site.site_title = "Iot Devices"

class ReadingInline(admin.TabularInline):
    model = Device.reading.through
    extra = 0


class DeviceInline(admin.TabularInline):
    model = Reading.device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "readings_count",
    )
    search_fields = (
        "name",
    )
    inlines = (ReadingInline,)

    def readings_count(self, inst):
        return inst.reading.count()
