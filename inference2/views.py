import json

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
import importlib
from inference2.Proofs import prove3
from inference2.models import Input
from models import Define3, Archives

from Proofs import new_prove



# Create your views here.

def current_archive():
    archive = Archives.objects.latest('archives_date')
    return archive

def index(request,archive=None):
    url_path=''
    if not archive:
        archive = current_archive()
        url_path = '/'
    else:
        url_path = '/archives/{}/'.format(archive.id)
    input = Input.objects.filter(archives_id=archive.id)
    result={}
    if request.method=='POST':
        post_data=request.POST.copy()
        prove_algorithm = importlib.import_module('.'+archive.algorithm,package='inference2.Proofs')
        post_data = prove_algorithm.get_result(request.POST.copy())
        result=json.dumps(post_data,cls=DjangoJSONEncoder)

    #rows = json.dumps(rows,cls=DjangoJSONEncoder)

    template_args = {'result':result,'input':input,'url_path':url_path}
    return render(request,"inference2/index.html",template_args)

def prove(request,archive=None):
    if not archive:
        archive = current_archive()
    result={}
    if request.method=='POST':
        post_data=request.POST.copy()
        prove_algorithm = importlib.import_module('.'+archive.algorithm,package='inference2.Proofs')
        post_data = prove_algorithm.get_result(request.POST.copy())
        result=json.dumps(post_data,cls=DjangoJSONEncoder)

    #rows = json.dumps(rows,cls=DjangoJSONEncoder)
    return result


def dictionary(request,archive=None):
    url_path = '/archives/'
    if not archive:
        archive = current_archive()
        url_path = '/'
    else:
        url_path = '/archives/{}/'.format(archive.id)
    dict=Define3.objects.filter(archives_id=archive.id)
    return render(request,"inference2/dict.html",{'result':dict,'url_path':url_path})

def archives(request):
    dict=Archives.objects.all()
    return render(request,"inference2/archives.html",{'result':dict})

def assign_archives(request,num=-1,type=None):
    if num==-1:
        return
    archive = Archives.objects.get(pk=num)
    if type:
        return globals()[type](request,archive)
    else:
        return index(request,archive)

