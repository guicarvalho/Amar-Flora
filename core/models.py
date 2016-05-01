# coding: utf-8

from django.utils.translation import ugettext_lazy as _

from django.db import models

from django.core.validators import MinValueValidator


class Partner(models.Model):
	name = models.CharField(_('Name'), max_length=50)
	phone = models.CharField(_('Phone'), max_length=11, blank=True, null=True)
	email = models.EmailField(_('E-mail'))
	benefit = models.CharField(_('Benefit'), max_length=100)

	class Meta:
		verbose_name = _('Partner')
		verbose_name_plural = _('Partners')

	def __str__(self):
		return self.name


class Associate(models.Model):
	name = models.CharField(_('Name'), max_length=50)
	rg = models.CharField(_('RG'), max_length=10)
	cpf = models.CharField(_('CPF'), max_length=11)
	birthday = models.DateField(_('Birthday'))
	phone = models.CharField(_('Phone'), max_length=11, blank=True, null=True)
	cell_phone = models.CharField(_('Cell Phone'), max_length=11, blank=True, null=True)
	street = models.CharField(_('Street'), max_length=100)
	number = models.IntegerField(_('Number'), null=True, blank=True, validators=[MinValueValidator(1)])
	complement = models.CharField(_('Complement'), max_length=35, blank=True, null=True)
	email = models.EmailField(_('E-mail'))

	class Meta:
		verbose_name = _('Associate')
		verbose_name_plural = _('Associates')


class News(models.Model):
	title = models.CharField(max_length=80)
	description = models.TextField()

	class Meta:
		verbose_name = _('News')
		verbose_name_plural = _('News')

	def __str__(self):
		return self.title


class Request(models.Model):
	OTHERS = 1
	SECURITY = 2
	LIGHTING = 3
	CONSTRUCTION = 4
	CLEANING = 5

	SUBJECT_CHOICES = (
		(OTHERS, _('Others')),
		(SECURITY, _('Security')),
		(LIGHTING, _('Lighting')),
		(CONSTRUCTION, _('Construction')),
		(CLEANING, _('Cleaning')),
	)

	OPEN = 'O'
	WAITING = 'W'
	CLOSED = 'C'

	STATUS_CHOICE = (
		(OPEN, _('Open')),
		(WAITING, _('Waiting')),
		(CLOSED, _('Closed')),
	)

	email = models.EmailField(_('E-mail'))
	name = models.CharField(_('Name'), max_length=50)
	phone = models.CharField(_('Phone'), max_length=11)
	street = models.CharField(_('Street'), max_length=100)
	number = models.IntegerField(_('Number'), null=True, blank=True, validators=[MinValueValidator(1)])
	complement = models.CharField(_('Complement'), max_length=35, blank=True, null=True)
	description = models.TextField(_('Description'))
	status = models.CharField(_('Status'), max_length=1, choices=STATUS_CHOICE, default=OPEN)
	subject = models.IntegerField(_('Subject'), choices=SUBJECT_CHOICES)

	class Meta:
		verbose_name = _('Request')
		verbose_name_plural = _('Requests')

	def __str__(self):
		return self.name


class Gallery(models.Model):
	title = models.CharField(max_length=80)
	description = models.TextField()
	date = models.DateField()


class Classified(models.Model):
	title = models.CharField(_('Title'), max_length=80)
	description = models.TextField(_('Description'))
	site = models.URLField(_('Site'))

	class Meta:
		verbose_name = _('Classified')
		verbose_name_plural = _('Classifieds')

	def __str__(self):
		return self.title
