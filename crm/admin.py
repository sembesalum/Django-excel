from django.contrib import admin

# Register your models here.

from .models import Employee

from import_export.admin import ImportExportActionModelAdmin

admin.site.register(Employee, ImportExportActionModelAdmin)