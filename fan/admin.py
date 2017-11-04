from django.contrib import admin

from fan.models import Fan


@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    pass
