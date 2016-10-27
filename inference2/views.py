import json
import os
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse
from django.conf import settings
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django_tools.middlewares import ThreadLocal
from django.views.decorators.csrf import csrf_exempt
import time
from django.db import transaction

from models import Output
import os
import importlib
from inference2.Proofs import prove3
from inference2.models import Input

from models import Define3, Archives

from Proofs import new_prove




def save_result(post_data):
    Output.objects.all().delete()
    Rows =[]
    for idx in xrange(15000-1):
        R = Output(col1=post_data["text_"+str(idx)+"_1"],
                col2=post_data["text_"+str(idx)+"_2"],
                col3=post_data["text_"+str(idx)+"_3"]
                )
        Rows.append(R)
    Output.objects.bulk_create(Rows)


# Create your views here.

def current_archive():
    archive = Archives.objects.latest('archives_date')
    return archive

def index(request,archive=None):
    url_path=''
    archive_date=''
    if not archive:
        archive = current_archive()
        url_path = '/'
    else:
        url_path = '/archives/{}/'.format(archive.id)
        archive_date = archive.archives_date
    input = Input.objects.filter(archives_id=archive.id)
    result={}
    if request.method=='POST':
        post_data=request.POST.copy()
        prove_algorithm = importlib.import_module('.'+archive.algorithm,package='inference2.Proofs')
        post_data = prove_algorithm.get_result(request.POST.copy(),request)
        post_data["type"]="prove"
        result=json.dumps(post_data,cls=DjangoJSONEncoder)
        save_result(post_data)

    #rows = json.dumps(rows,cls=DjangoJSONEncoder)

    template_args = {'result':result,'input':input,'url_path':url_path,'archive_date':archive_date}
    return render(request,"inference2/index.html",template_args)


def stream_response_generator(request):
    for x in range(1,11):
        yield "%s\n" % x  # Returns a chunk of the response to the browser
        request.session['idx'] = x
        request.session.modified = True 
        
        request.session.save()
        time.sleep(1)
    


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

def manual(request):
    filename = os.path.join(settings.MANUAL_PATH)
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename='+os.path.basename(filename)
    return response

def getdict(request,archive=None):
    if not archive:
        archive = current_archive()

    filename = os.path.join(settings.DICT_DIRS,archive.algorithm+".csv")
    if not os.path.exists(filename):
        return HttpResponse("No CSV found for Algorithm %s" %archive.algorithm )
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename='+os.path.basename(filename)
    return response

def progress(request):
       
    return HttpResponse(json.dumps({"K":request.session['idx']}), content_type="application/json")

def progressbar_send(request,strt,stp,k):
    if request is not None:
            request.session.modified = True
            request.session['strt'] = strt
            request.session['stp'] = stp
            request.session['idx'] = [strt,stp,k]
            request.session.modified = True
            request.session.save()