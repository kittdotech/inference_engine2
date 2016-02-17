from django.contrib import admin
from inference2.models import Define3
from django.contrib.auth.models import User

from django.contrib import admin

from inference2.models import Define3
from django.contrib import admin

from .actions import export_as_csv_action
from .actions import change_text_to_symbol_action
from .actions import change_symbol_to_text_action
from .actions import export_as_json_action
from .actions import export_as_xml_action
from .actions import export_as_yaml_action


admin.site.add_action(export_as_csv_action)
admin.site.add_action(change_text_to_symbol_action)
admin.site.add_action(change_symbol_to_text_action)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','type','word', 'rel','definition')
    empty_value_display = ""
    ordering = ("id",)
    list_per_page = 1000



admin.site.register(Define3, AuthorAdmin)

