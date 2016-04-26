from django.contrib import admin
from django.core import serializers
from django.http import HttpResponse

from .utils import json_to_csv


def serialize_queryset(queryset, format):
    data = serializers.serialize(format, queryset)
    return data


def export(queryset, format):
    if format == "csv":
        # TODO: Less hacky
        import json

        data = serialize_queryset(queryset, "json")
        data = json.loads(data)
        dataFlattened = []

        for item in data:
            flattednedItem = item["fields"]
            flattednedItem["pk"] = item["pk"]
            # flattednedItem["model"] = item["model"]
            dataFlattened.append(flattednedItem)
        data = json.dumps(dataFlattened)
        data = json_to_csv(data)
    else:
        data = serialize_queryset(queryset, format)

    response = HttpResponse(data, content_type="application/x-download")
    response["Content-Disposition"] = "attachment;filename=export.{extention}".format(extention=format.lower())

    return response


def changesymbol(queryset, mode):
    import json
    # data = serialize_queryset(queryset, "json")
    # data = json.loads(data)
    # for item in data:
    #	print
    symbol_map = (
        ('>>', unichr(8835)),
        ('ta^', unichr(8868)),
        ('co^', unichr(8869)),
        (';', unichr(172)),
        ('<>', unichr(8801)),
        ('c^', unichr(8658)),
        ('#', unichr(8703)),
        ('i^', unichr(8866)),
        ('>', unichr(8594)),
        ('nf^', unichr(8876)),
        ('ed^', unichr(8891)),
        ('+', unichr(8744)),
        ('&&', unichr(8896)),
        ('@', unichr(8855)),
        ('if^', unichr(8660)),
        ('ne', u"\u2260"),
        ('l1', u"\u2081"),
        ('l2', u"\u2082"),
        ('l3', u"\u2083"),
        ('l7', u"\u2087"),
        ('l8', u"\u2088"),
        ('ua', u"\u1d43"),
        ('ub', u"\u1d47"),
        ('uc', u"\u1d9c"),
        ('ud', u"\u1d48"),
        ('ue', u"\u1d49"),
        ('uf', u"\u1da0"),
        ('ug', u"\u1d4d"),
        ('ui', u"\u2071"),
        ('uk', u"\u1d4f"),
        ('um', u"\u1d50"),
        ('un', u"\u207f"),
        ('uo', u"\u1d52"),
        ('up', u"\u1d56"),
        ('ut', u"\u1d57"),
        ('uv', u"\u1d5b"),
        ('uu', u"\u1d58"),
        ('uw', u"\u02b7"),
        ('uy', u"\u02b8"),
        ('uj', u"\u02B2"),
        ('ul', u"\u02E1"),
        ('ur', u"\u02b3"),
        ('us', u"\u02e2"),
        ('uh', u"\u02b0"),
        )
    if mode == 'TtoS':
        for x in queryset:
            original_text = x.definition
            if original_text:
                for (T,S) in symbol_map:
                    if T in original_text:
                        original_text = original_text.replace(T, S)
            x.definition = original_text
            x.save()
    if mode == 'StoT':
        for x in queryset:
            original_text = x.definition
            if original_text:
                for (T,S) in symbol_map:
                    if S in original_text:
                        original_text = original_text.replace(S, T)
            x.definition = original_text
            x.save()


def export_as_csv_action(modeladmin, request, queryset):
    return export(queryset, format="csv")


export_as_csv_action.short_description = "Export selected items to CSV"


def change_text_to_symbol_action(modeladmin, request, queryset):
    return changesymbol(queryset, mode="TtoS")


change_text_to_symbol_action.short_description = "Change Text to Symbol"


def change_symbol_to_text_action(modeladmin, request, queryset):
    return changesymbol(queryset, mode="StoT")


change_symbol_to_text_action.short_description = "Change Symbol to Text"


def export_as_json_action(modeladmin, request, queryset):
    return export(queryset, format="json")


export_as_json_action.short_description = "Export selected items to JSON"


def export_as_xml_action(modeladmin, request, queryset):
    return export(queryset, format="xml")


export_as_xml_action.short_description = "Export selected items to XML"


def export_as_yaml_action(modeladmin, request, queryset):
    return export(queryset, format="yaml")


export_as_yaml_action.short_description = "Export selected items to YAML"
