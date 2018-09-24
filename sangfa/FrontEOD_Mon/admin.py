from django.contrib import admin
from .models import Host, Tool

# Register your models here.


class HostAdmin(admin.ModelAdmin):
    list_display = ('user', 'hostname', 'description')


class ToolAdmin(admin.ModelAdmin):
    list_display = ('tool_name', 'host', 'description')


admin.site.register(Host, HostAdmin)
admin.site.register(Tool, ToolAdmin)
