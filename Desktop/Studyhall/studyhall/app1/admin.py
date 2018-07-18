# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Course,Student,Studyhall,Enquries,Expense

# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Studyhall)
admin.site.register(Enquries)
admin.site.register(Expense)
