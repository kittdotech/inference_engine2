from django.shortcuts import render
from django.shortcuts import render
from inference2.models import Define3
from django.core.serializers.json import DjangoJSONEncoder
from . import guided_proof
from . import  proof2
import json
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.


def index(request):
    result={}
    if request.method=='POST':
        post_data=request.POST.copy()
        post_data = proof2.get_result(request.POST.copy())
        result=json.dumps(post_data,cls=DjangoJSONEncoder)

    #rows = json.dumps(rows,cls=DjangoJSONEncoder)
    return render(request,"inference2/index.html",{'result':result})