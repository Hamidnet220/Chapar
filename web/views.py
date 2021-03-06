import os
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.conf import settings
from .models import *
from .forms import *    
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
    if len(recived)==0 and len(sent)==0:
        return HttpResponse("<h1> نامه ای با این مشخصات یافت نشد.</h1>")
    context={
        'rs':recived,
        'sd':sent,
    }
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


class ReciveLetterView(FormView):
    template_name='input_forms.html'
    form_class=Recive_Letter_form
    success_url='recive/addnew/'

    def form_valid(self, form):
        form.add_record()
        return super().form_valid(form)

class SendLetterView(FormView):
    template_name='input_forms.html'
    form_class=Send_Letter_form
    success_url='/home/'

    def form_valid(self, form):
        form.add_record()
        return super().form_valid(form)

def delete_view(request,my_id,*args,**kwargs):
    obj=Recive.objects.get(id=my_id).delete()
    return HttpResponse("<h1>نامه مورد نظر حذف شد<h1>")

class OrganizationView(FormView):
    template_name='input_forms.html'
    form_class=Organization_form
    success_url = '/chapar/organization/new'
    
    def form_valid(self, form):
        form.add_record()
        return super().form_valid(form)

    
    
    