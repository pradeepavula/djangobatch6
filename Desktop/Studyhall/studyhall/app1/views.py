# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app1.models import Studyhall,Expense,Enquries

# Create your views here.

def view_index(request):
	studyhalls = Studyhall.objects.all()
	expense = Expense.objects.all()
	enquiry = Enquries.objects.all()

	return render(request,"app1/index.html",{ "halls":studyhalls,"exps": expense,"enqs":enquiry})

def view_studyhall(request):
	studyhalls = Studyhall.objects.all()
	return render(request,"app1/index.html",{"studyhalls":studyhalls})