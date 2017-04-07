
from django.contrib import admin
from django import forms
import os.path, pkgutil
from inference2 import Proofs
from inference2.models import Define3, Archives
from django.contrib.auth.models import User
from django.forms import ModelForm

from django.contrib import admin

try:
    from admin_import.options import add_import
except ImportError:
    pass
else:
    add_import(admin.ModelAdmin, add_button=True)
from inference2.models import Define3,Input
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
    list_display = ('id','extra','type','word', 'rel','')
    empty_value_display = ""
    ordering = ("id",)
    list_per_page = 1000



#admin.site.register(Define3, AuthorAdmin)
class MyDefineImporter(ModelForm):

    class Meta:
        model = Define3
        fields = ('id','extra','type', 'word', 'rel','definition','archives')


class MyDefineForm(ModelForm):
    class Meta:
        model = Define3
        fields = ('id','extra','type', 'word', 'rel','definition', 'archives')


class MyDefine(ImportCSVModelAdmin):
    importer_class = MyDefineImporter
    form = MyDefineForm
    list_display = ('id','extra','type','word', 'rel','definition')
    empty_value_display = ""
    ordering = ("id",)
    list_per_page = 1000

class MyInputImporter(ModelForm):

    class Meta:
        model = Input
        fields = ('col1','col2','col3','archives')


class MyInputForm(ModelForm):
    class Meta:
        model = Input
        fields = ('col1','col2','col3','archives')


class MyInput(ImportCSVModelAdmin):
    importer_class = MyInputImporter
    form = MyInputForm
    list_display = ('col1','col2','col3')
    empty_value_display = ""
    ordering = ("id",)
    list_per_page = 1000


class MyArchiveImporter(ModelForm):

    class Meta:
        model = Archives
        fields = ('archives_date', 'algorithm')


class MyArchiveForm(ModelForm):
    pkgpath = os.path.dirname(Proofs.__file__)
    MY_CHOICES = [(name,name) for _, name, _ in pkgutil.iter_modules([pkgpath])]
    algorithm = forms.ChoiceField(choices=MY_CHOICES)
    class Meta:
        model = Archives
        fields = ('archives_date', 'algorithm')


class MyArchive(ImportCSVModelAdmin):
    importer_class = MyArchiveImporter
    form = MyArchiveForm
    list_display = ('archives_date', 'algorithm')
    ordering = ("archives_date",)
    list_per_page = 1000
    empty_value_display = ""

"""
class MyArchivesForm(admin.ModelAdmin):
    list_display = ('archives_date','algorithm')
    ordering = ("archives_date",)
    list_per_page = 1000
"""
admin.site.register(Define3, MyDefine)
admin.site.register(Input,MyInput)
admin.site.register(Archives,MyArchive)
