from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Disasters


class DisastersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pk', 'country', 'disaster_type', 'people_died', 'year')


admin.site.register(Disasters, DisastersAdmin)
