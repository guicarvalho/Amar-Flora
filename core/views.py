# coding: utf-8

from django.contrib import messages

from django.shortcuts import render, redirect

from django.utils.translation import ugettext_lazy as _

from core.forms import AssociateForm, RequestForm

from core.models import Associate, News, Partner, Classified, Gallery


def home(request):
 	return render(request, 'core/home.html')


def list_associate(request):
	associates = Associate.objects.filter(approved=True)

	return render(request, 'core/associate_list.html', {
		'associates': associates
	})


def new_associate(request):
	form = AssociateForm(request.POST or None)

	if request.POST:
		if form.is_valid():
			form.save()

			storage = messages.get_messages(request)
			storage.used = True
			
			messages.success(request, _('Form submitted successfully. Waiting for approval!'))

			return redirect('associate-list')
		else:
			messages.error(request, _('The form contains errors.'))

	return render(request, 'core/associate_new.html', {
		'form': form
	})


def list_news(request):
	news = News.objects.filter()

	return render(request, 'core/news_list.html', {
		'list_news': news
	})


def list_partner(request):
	partners = Partner.objects.filter()

	return render(request, 'core/partner_list.html', {
		'partners': partners
	})


def list_classified(request):
	classifieds = Classified.objects.filter()

	return render(request, 'core/classified_list.html', {
		'classifieds': classifieds
	})


def new_request(request):
	form = RequestForm(request.POST or None)

	if request.POST:
		if form.is_valid():
			form.save()

			messages.success(request, 'Requisição feita com sucesso')

			return redirect('request-new')
		else:
			messages.error(request, 'O formulário contém erros.')

	return render(request, 'core/request_new.html', {
		'form': form
	})


def list_gallery(request):
	events = Gallery.objects.filter()

	return render(request, 'core/gallery_list.html', {
		'events': events
	})
