# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models  import *

# Create your models here.
class Todolist(models.Model):
    name=models.CharField(max_length=128)
    creation_date=models.DateField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    def __unicode__(self):
        return self.name

class Todoitem(models.Model):
    description=models.CharField(max_length=300)
    completed=models.BooleanField(default=False)
    due_by=models.DateField(auto_now=True)
    todolist=models.ForeignKey(Todolist)
    def __unicode__(self):
        return self
