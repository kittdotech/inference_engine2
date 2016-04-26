
from django.contrib import admin

from inference2.models import Define3
from django.contrib.auth.models import User
from django.forms import ModelForm

from django.contrib import admin

try:
    from admin_import.options import add_import
except ImportError:
    pass
else:
    add_import(admin.ModelAdmin, add_button=True)
from inference2.models import Define3
from django.contrib import admin
from .actions import export_as_csv_action
from .actions import change_text_to_symbol_action
from .actions import change_symbol_to_text_action
from .actions import export_as_json_action
from .actions import export_as_xml_action
from .actions import export_as_yaml_action

from admincsv import ImportCSVModelAdmin
admin.site.add_action(export_as_csv_action)
admin.site.add_action(change_text_to_symbol_action)
admin.site.add_action(change_symbol_to_text_action)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','extra','type','word', 'rel','definition')
    empty_value_display = ""
    ordering = ("id",)
    list_per_page = 1000



#admin.site.register(Define3, AuthorAdmin)
class MyAdminImporter(ModelForm):

    class Meta:
        model = Define3
        fields = ('id','extra','type', 'word', 'rel','definition')


class MyAdminForm(ModelForm):
    class Meta:
        model = Define3
        fields = ('id','extra','type', 'word', 'rel','definition')


class MyAdmin(ImportCSVModelAdmin):
    importer_class = MyAdminImporter
    form = MyAdminForm
    list_display = ('id','extra','type','word', 'rel','definition')
    empty_value_display = ""
    ordering = ("id",)
    list_per_page = 1000

admin.site.register(Define3, MyAdmin)

