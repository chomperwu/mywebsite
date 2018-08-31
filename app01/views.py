from django.shortcuts import render,HttpResponse
from app01 import models
# Create your views here.

def home(request,userman):
    return HttpResponse("OK,it' %s ." %userman)

def news(request,nid1,nid2):
    return HttpResponse(nid1+nid2)

def db_handle(request):
    #models.userinfo.objects.filter(name='jojo').delete()
    #models.userinfo.objects.filter(name='jojo').update(age=30)

    #models.userinfo.objects.create(name=request.POST['username'],
    #                               age=request.POST['userage']
    #                               )
    if request.POST.get('username') and request.POST.get('userage'):
        models.userinfo.objects.create(name=request.POST.get('username'),
                                       age=request.POST.get('userage')
                                      )
    user_list_obj = models.userinfo.objects.all()
    print request.POST.get('userage')
    print request.POST
    #print type(request.POST)
    return render(request,'t1.html',{'li':user_list_obj})
