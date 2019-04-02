from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from django.forms import formset_factory
from web.models import *




class Organization_form(forms.Form):
    title        = forms.CharField(label="عنوان سازمان:",max_length=100)
    tel          = forms.CharField(label="تلفن تماس:",max_length=19)
    fax          = forms.CharField(label="فکس:",max_length=19)

    def  add_record(self):
        user=User.objects.first()
        self.cleaned_data.update({'add_by_usr':user})  
        print(self.cleaned_data)
        obj=self.cleaned_data
        Organization.objects.create(**obj)



class Recive_Letter_form(forms.Form):
    organization = forms.ModelChoiceField(Organization.objects.all(),label="شرکت یا سازمان:")
    title        = forms.CharField(label="عنوان:")
    summery      = forms.CharField(label="خلاصه نامه:")
    recive_date  = forms.DateTimeField(label="تاریخ نامه:")
    recive_number= forms.CharField(label="شماره نامه:")
    description  = forms.CharField(label="توضیحات")
    # recive_file  = forms.FileField()

    def  add_record(self):
        user=User.objects.first()
        self.cleaned_data.update({'add_by_usr':user})  
        Recive.objects.create(**self.cleaned_data)


class Send_Letter_form(forms.Form):
    organization = forms.ModelChoiceField(Organization.objects.all(),label="شرکت یا سازمان:")
    title        = forms.CharField(label="عنوان:")
    summery      = forms.CharField(label="خلاصه نامه:")
    send_date  = forms.DateTimeField(label="تاریخ نامه:")
    send_number= forms.CharField(label="شماره نامه:")
    description  = forms.CharField(label="توضیحات")
    # recive_file  = forms.FileField()

    def  add_record(self):
        user=User.objects.first()
        self.cleaned_data.update({'add_by_usr':user})  
        Send.objects.create(**self.cleaned_data)


