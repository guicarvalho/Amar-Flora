# coding: utf-8

from django import forms

from core.models import Associate


class AssociateForm(forms.ModelForm):
	class Meta:
		model = Associate
		fields = '__all__'
