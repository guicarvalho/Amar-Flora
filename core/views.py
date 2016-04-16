#coding: utf-8

from django.shortcuts import render


def home(request):
	context = {'user': 'Teste', 'age': 21}

	return render(request, 'core/home.html', context)


def go_gallery(request):
	context = {}
	return render(request, 'core/gallery.html', context)
