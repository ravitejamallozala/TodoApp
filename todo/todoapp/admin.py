# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from todoapp.models import *
from django.contrib import admin

# Register your models here.

admin.site.register(Todolist)
admin.site.register(Todoitem)