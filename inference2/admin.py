from django.contrib import admin
from inference2.models import Define3
from django.contrib.auth.models import User

from django.contrib import admin
from inference2.models import Define3
from django.contrib import admin

from admin_exporter.actions import export_as_csv_action
from admin_exporter.actions import export_as_json_action
from admin_exporter.actions import export_as_xml_action
from admin_exporter.actions import export_as_yaml_action


admin.site.add_action(export_as_csv_action)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('type','word', 'rel','definition')

admin.site.register(Define3, AuthorAdmin)