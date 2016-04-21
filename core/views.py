# coding: utf-8

from django.contrib import messages

from django.shortcuts import render

from core.forms import AssociateForm

from core.models import Associate, News


def home(request):
 	return render(request, 'core/home.html')


def list_associate(request):
	associates = Associate.objects.filter()

	return render(request, 'core/associate_list.html', {
		'associates': associates
	})


def new_associate(request):
	form = AssociateForm(request.POST or None)

	if (request.POST):
		if (form.is_valid()):
			form.save()

			messages.success(request, 'Seus dados foram inviados!')
		else:
			messages.error(request, 'O formulário contém erros.')

	return render(request, 'core/associate_new.html', {
		'form': form
	})


def list_news(request):
	news = News.objects.filter()

	return render(request, 'core/news_list.html', {
		'news': news
	})
