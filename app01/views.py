from django.shortcuts import render,HttpResponse
from app01 import models
# Create your views here.

def home(request):
    return HttpResponse('OK')

def news(request,nid1,nid2):
    return HttpResponse(nid1+nid2)

def db_handle(request):
    #models.userinfo.objects.create(name='recoba',age=40)
    #models.userinfo.objects.filter(name='jojo').delete()
    #models.userinfo.objects.filter(name='jojo').update(age=30)
    user_list_obj = models.userinfo.objects.all()
    #for line in user_list_obj:
    #    print line.name
    return render(request,'t1.html',{'li':user_list_obj})