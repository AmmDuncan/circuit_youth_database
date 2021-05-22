from django.contrib import admin

from .models import (Local, Executive, Member)


# Register your models here.
@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Executive)
class ExecutiveAdmin(admin.ModelAdmin):
    list_display = ["name", "local", "position"]
    list_filter = ["local"]


@admin.register(Member)
class ExecutiveAdmin(admin.ModelAdmin):
    list_display = ["name", "local"]
    list_filter = ["local"]