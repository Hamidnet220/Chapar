from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from itertools import chain
from .models import *
from django.contrib.auth.admin import User
import json
# Create your views here.
def get_recives(request,*args,**kwargs):
    obj=Recive.objects.all()
    context={
        "object":obj
    }
    return render(request,'recive.html',context)

# get all sent letter
def get_sends(request,*args,**kwargs):
    obj=Send.objects.all()
    print(obj)
    context={
        "object":obj
    }
    return render(request,'send.html',context)

#Search-letter by title
def search_letter(request,*args,**kwargs):
    recived = Recive.objects.filter(title__contains=request.GET['search_value'])
    sent    = Send.objects.filter(title__contains=request.GET['search_value'])
    print(recived)
    print(sent)
    if len(recived)==0 and len(sent)==0:
        return HttpResponse("<h1> نامه ای با این مشخصات یافت نشد.</h1>")
    context={
        'rs':recived,
        'sd':sent,
    }
    print(context)
    return render (request,"search_letter.html",context)

def get_letter_by_id(request,my_id):
    obj=Recive.objects.get(id=my_id)
    context={
        'object':obj
    }
    return render (request,"letter_detail.html",context)

def home_view(request,*args,**kwargs):
    return render(request,"home.html",{})

def contact_view(request,*args,**kwargs):
    return HttpResponse('<h1>Contact Page</h>')

def chapar_view(request,*args,**kwargs):
    return HttpResponse('<h1>You are in the Chapar page</h1>')

def about_view(request,*args,**kwargs):
    return render(request,"about.html",{})


def new_letter(request,*args,**kwargs):
    return render(request,"new_letter.html",{})

#TODO:validation input data
def create_letter_view(request,*args,**kwargs):
    print(request.POST)
    new_user=User.objects.first()
    new_title=request.POST['title']
    new_summery=request.POST['summery']
    new_recive_date=request.POST['recive_date']
    new_revice_number=request.POST['recive_number']
    Recive.objects.create(add_by_usr=new_user,title=new_title,summery=new_summery,recive_date=new_recive_date,
                        recive_number=new_revice_number,description='ندارد')
    
    return render(request,"new_letter.html",{})