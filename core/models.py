# coding: utf-8

from django.db import models

from django.core.validators import MinValueValidator


class Partner(models.Model):
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=11, blank=True, null=True)
	email = models.EmailField()
	benefit = models.CharField(max_length=100)


class Associate(models.Model):
	name = models.CharField(max_length=50)
	rg = models.CharField(max_length=10)
	cpf = models.CharField(max_length=11)
	birthday = models.DateField()
	phone = models.CharField(max_length=11, blank=True, null=True)
	cell_phone = models.CharField(max_length=11, blank=True, null=True)
	street = models.CharField(max_length=100)
	number = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)])
	complement = models.CharField(max_length=35, blank=True, null=True)
	email = models.EmailField()


class News(models.Model):
	title = models.CharField(max_length=80)
	description = models.TextField()


class Request(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=11)
	street = models.CharField(max_length=100)
	number = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)])
	complement = models.CharField(max_length=35, blank=True, null=True)
	description = models.TextField()
	status = models.CharField(max_length=1)
	subject = models.IntegerField()


class Gallery(models.Model):
	title = models.CharField(max_length=80)
	description = models.TextField()
	date = models.DateField()


class Classified(models.Model):
	title = models.CharField(max_length=80)
	description = models.TextField()
