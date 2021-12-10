from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class clientmst(models.Model):
    clientid = models.AutoField(auto_created=True, primary_key=True)
    clientname = models.CharField(max_length=30, null=True)
    created_at = models.DateTimeField(null=True, default=datetime.now())
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return '%s' % self.clientname

class Project(models.Model):
    Projectid= models.AutoField(auto_created=True,primary_key=True)
    Projectname =models.CharField(max_length=50,null=True)
    created_at = models.DateTimeField(null=True, default=datetime.now())
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    updated_at=models.DateTimeField(null=True, default=datetime.now())

    def __str__(self):
        return '%s' % self.Projectname



            








