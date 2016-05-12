from django.shortcuts import render
from django.shortcuts import render
from inference2.models import Define3,Input
from django.core.serializers.json import DjangoJSONEncoder
from . import guided_proof
from . import  prove3,new_prove
import json
from django.http import HttpResponse,HttpResponseRedirect
from models import Define3
# Create your views here.


def index(request):
    input = Input.objects.all()
    result={}
    if request.method=='POST':
        post_data=request.POST.copy()
        post_data = new_prove.get_result(request.POST.copy())
        result=json.dumps(post_data,cls=DjangoJSONEncoder)

    #rows = json.dumps(rows,cls=DjangoJSONEncoder)


    return render(request,"inference2/index.html",{'result':result,'input':input})

def prove(request):
    result={}
    if request.method=='POST':
        post_data=request.POST.copy()
        post_data = prove3.get_result(request.POST.copy())
        result=json.dumps(post_data,cls=DjangoJSONEncoder)

    #rows = json.dumps(rows,cls=DjangoJSONEncoder)
    return result


def dictionary(request):
    dict=Define3.objects.all()
    return render(request,"inference2/dict.html",{'result':dict})