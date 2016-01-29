from django.shortcuts import render
from django.shortcuts import render
from inference2.models import Define3
from django.core.serializers.json import DjangoJSONEncoder

import json
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request):
    rows=Define3.objects.all()
    #rows = json.dumps(rows,cls=DjangoJSONEncoder)
    return render(request,"inference2/index.html",{'rows':rows})