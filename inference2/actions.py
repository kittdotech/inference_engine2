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
        ('b^', unichr(8703)),
        ('i^', unichr(8866)),
        ('>', unichr(8594)),
        ('nf^', unichr(8876)),
        ('ed^', unichr(8891)),
        ('+', unichr(8744)),
        ('&&', unichr(8896)),
        ('@', unichr(8855)),
        ('if^', unichr(8660)),

        ('-a', u"\u1d43"),
        ('-b', u"\u1d47"),
        ('-c', u"\u1d9c"),
        ('-d', u"\u1d48"),
        ('-e', u"\u1d49"),
        ('-f', u"\u1da0"),
        ('-g', u"\u1d4d"),
        ('-i', u"\u2071"),
        ('-k', u"\u1d4f"),
        ('-m', u"\u1d50"),
        ('-n', u"\u207f"),
        ('-o', u"\u1d52"),
        ('-p', u"\u1d56"),
        ('-t', u"\u1d57"),
        ('-v', u"\u1d5b"),
        ('-u', u"\u1d58"),
        ('-w', u"\u02b7"),
        ('-y', u"\u02b8"),
        ('-j', u"\u02B2"),
        ('-l', u"\u02E1"),
        ('-r', u"\u02b3"),
        ('-s', u"\u02e2"),
        ('-h', u"\u02b0"),
        ('zzz', u"\u2260"),
        )
    if mode == 'TtoS':
        for x in queryset:
            original_text_definition = x.definition
            original_text_word = x.word
            original_text_rel = x.rel
            if original_text_definition or original_text_word or original_text_rel:
                for (T,S) in symbol_map:
                    if T in original_text_definition:
                        original_text_definition = original_text_definition.replace(T, S)
                    if T in original_text_word:
                        original_text_word = original_text_word.replace(T, S)
                    if T in original_text_rel:
                        original_text_rel = original_text_rel.replace(T, S)


            x.definition = original_text_definition
            x.word = original_text_word
            x.rel = original_text_rel
            x.save()
    if mode == 'StoT':
        for x in queryset:

            original_text_definition = x.definition
            original_text_word = x.word
            original_text_rel = x.rel
            if original_text_definition or original_text_word or original_text_rel:
                for (T,S) in symbol_map:
                    if S in original_text_definition:
                        original_text_definition = original_text_definition.replace(S, T)
                    if S in original_text_word:
                        original_text_word = original_text_word.replace(S, T)
                    if S in original_text_rel:
                        original_text_rel = original_text_rel.replace(S, T)
            x.definition = original_text_definition
            x.word = original_text_word
            x.rel = original_text_rel
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
