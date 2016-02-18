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
			#flattednedItem["model"] = item["model"]
			dataFlattened.append(flattednedItem)
		data = json.dumps(dataFlattened)
		data = json_to_csv(data)
	else:
		data = serialize_queryset(queryset, format)

	response = HttpResponse(data, content_type="application/x-download")
	response["Content-Disposition"] = "attachment;filename=export.{extention}".format(extention=format.lower())

	return response

def changesymbol(queryset,mode):
	import json
	#data = serialize_queryset(queryset, "json")
	#data = json.loads(data)
	#for item in data:
	#	print

	if mode=='TtoS':
		for x in queryset:
			original_text = x.definition
			if original_text:

				if '>>' in original_text:
					original_text=original_text.replace('>>',unichr(8835))
				if 'ta^' in original_text:
					original_text=original_text.replace('ta^',unichr(8868))
				if 'co^' in original_text:
					original_text=original_text.replace('co^',unichr(8869))
				if ';' in original_text:
					original_text=original_text.replace(';',unichr(172))
				if '<>' in original_text:
					original_text=original_text.replace('<>',unichr(8801))
				if ' c^' in original_text:
					original_text=original_text.replace('c^',unichr(8658))
				if '#' in original_text:
					original_text=original_text.replace('#',unichr(8703))
				if 'i^' in original_text:
					original_text=original_text.replace('i^',unichr(8866))
				if '>' in original_text:
					original_text=original_text.replace('>',unichr(8594))
				if 'nf^' in original_text:
					original_text=original_text.replace('nf^',unichr(8876))
				if 'ed^' in original_text:
					original_text=original_text.replace('ed^',unichr(8891))
				if '+' in original_text:
					original_text=original_text.replace('+',unichr(8744))
				if '&&' in original_text:
					original_text=original_text.replace('&&',unichr(8896))
				if '@' in original_text:
					original_text=original_text.replace('@',unichr(8855))
				if 'if^' in original_text:
					original_text=original_text.replace('if^',unichr(8660))
			x.definition = original_text
			x.save()
	if mode=='StoT':
		for x in queryset:
			original_text = x.definition
			if original_text:
				if  unichr(8835)in original_text:
					original_text=original_text.replace(unichr(8835),'>>')
				if  unichr(8868)in original_text:
					original_text=original_text.replace(unichr(8868),'ta^')
				if  unichr(8869)in original_text:
					original_text=original_text.replace(unichr(8869),'co^' )
				if  unichr(172)in original_text:
					original_text=original_text.replace(unichr(172),';')
				if  unichr(8801)in original_text:
					original_text=original_text.replace(unichr(8801),'<>' )
				if  unichr(8658)in original_text:
					original_text=original_text.replace(unichr(8658),' c^')
				if  unichr(8703)in original_text:
					original_text=original_text.replace(unichr(8703),'#')
				if  unichr(8866)in original_text:
					original_text=original_text.replace(unichr(8866),'i^')
				if unichr(8594)in original_text:
					original_text=original_text.replace(unichr(8594),'>' )
				if  unichr(8876)in original_text:
					original_text=original_text.replace(unichr(8876),'nf^')
				if  unichr(8891)in original_text:
					original_text=original_text.replace(unichr(8891),'ed^')
				if  unichr(8744)in original_text:
					original_text=original_text.replace(unichr(8744),'+')
				if  unichr(8896)in original_text:
					original_text=original_text.replace(unichr(8896),'&&')
				if  unichr(8855)in original_text:
					original_text=original_text.replace(unichr(8855),'@')
				if  unichr(8660)in original_text:
					original_text=original_text.replace(unichr(8660),'if^')
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
