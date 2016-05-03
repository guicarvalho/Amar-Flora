# coding: utf-8

from django import forms

from core.models import Associate, Request


class AssociateForm(forms.ModelForm):
	class Meta:
		model = Associate
		fields = '__all__'


class RequestForm(forms.ModelForm):
	class Meta:
		model = Request
		fields = '__all__'
		exclude = ('status',)
