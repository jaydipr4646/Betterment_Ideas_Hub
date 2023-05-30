from django.contrib import admin
from core import models
from django.contrib.admin import AdminSite

# Register your models here.



class InnovateModelAdmin(admin.ModelAdmin):
    class Meta:
        model = models.InnovateModel

    list_display = [
        'id',
        'name',
        'email'
    ]


admin.site.register(models.InnovateModel, InnovateModelAdmin)