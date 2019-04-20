from django.contrib import admin
from .models import *
# Register your models here.

class execution_detailsAdmin(admin.ModelAdmin):
    class meta:
        execution_details

class execution_summaryAdmin(admin.ModelAdmin):
    class meta:
        execution_summary

admin.site.register(execution_details,execution_detailsAdmin)
admin.site.register(execution_summary,execution_summaryAdmin)