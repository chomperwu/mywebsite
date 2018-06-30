from django.shortcuts import render,HttpResponse
from app01 import models
# Create your views here.

def home(request):
    return HttpResponse('OK')

def news(request,nid1,nid2):
    return HttpResponse(nid1+nid2)

def db_handle(request):
    models.userinfo.objects.create(name='jojo',age=27)
    #models.userinfo.objects.filter(name='jojo').delete()
    models.userinfo.objects.filter(name='jojo').update(age=30)
    return HttpResponse('inter')