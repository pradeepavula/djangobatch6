# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Studyhall(models.Model):
	name=models.CharField(max_length=50)
	area=models.TextField(max_length=250)

	def __str__(self):

		return "%s,%s"%(self.name,self.area)

	class Meta:
		db_table = "Studyhall"



class  Course(models.Model):
	name= models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Student(models.Model):
	name=models.CharField(max_length=250)
	address = models.TextField(max_length=250)
	phone = models.CharField(max_length=10)
	email = models.CharField(max_length=250)

	def __str__(self):

		return self.name


class Expense(models.Model):
	name= models.CharField(max_length=250)
	dateofexpense= models.DateTimeField()
	name_studyhall= models.ForeignKey(Studyhall)
	desc = models.TextField(max_length=250)
	value = models.IntegerField()

	def __str__(self):

		return "%s,%s,%s,%s,%s"%(self.name,self.dateofexpense,self.name_studyhall,self.desc,self.value)



	class Meta:
		db_table = "Expenses"


class Enquries(models.Model):
	name=models.CharField(max_length=50)
	course=models.ForeignKey(Course)
	student= models.ForeignKey(Student)

	def __str__(self):
		return "%s,%s,%s"%(self.name,self.course,self.student)

	class Meta:
		db_table = "Enquries"