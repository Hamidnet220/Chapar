from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.admin import User
# Create your models here.
def empty_validate_event(value):
    if len(value)<=2:
        raise ValidationError(("You can not leave this field empty!"),params={'value':value},)

class Recive(models.Model):
    add_by_usr   = models.ForeignKey(User,on_delete=models.CASCADE)
    title        = models.CharField(max_length = 150,validators=[empty_validate_event])
    summery      = models.TextField(blank=True)
    recive_date  = models.DateTimeField()
    recive_number= models.CharField(max_length = 150)
    description  = models.TextField(blank=True,null=True)

    def __str__(self):
        return "{}-{}".format(self.title,self.recive_date)
    
class Send(models.Model):
    add_by_usr   = models.ForeignKey(User,on_delete=models.CASCADE)
    title        = models.CharField(max_length = 150,validators=[empty_validate_event])
    summery      = models.TextField(blank=True)
    send_date  = models.DateTimeField()
    send_number= models.CharField(max_length = 150)
    description  = models.TextField(blank=True,null=True)

    def __str__(self):
        return "{}-{}".format(self.title,self.send_date)