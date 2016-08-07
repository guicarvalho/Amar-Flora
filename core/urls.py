# coding: utf-8

from django.conf.urls import url

from core.views import (home, list_associate, new_associate,
                        list_news, list_partner, list_classified,
                        new_request, list_gallery, association_information,
                        page_construction, detail_gallery, detail_news)

urlpatterns = [
    url(r'^$', home, name='home'),

    url(r'^associate/$', list_associate, name='associate-list'),
    url(r'^associate/new/$', new_associate, name='associate-new'),
    url(r'^page-construction/$', page_construction, name='page-construction'),

    url(r'^news/$', list_news, name='news-list'),
    url(r'^news/detail/(?P<id>\d+)/$', detail_news, name='detail-news'),

    url(r'^partner/$', list_partner, name='partner-list'),

    url(r'^classified/$', list_classified, name='classified-list'),

    url(r'^request/new/$', new_request, name='request-new'),

    url(r'^gallery/$', list_gallery, name='gallery-list'),
    url(r'^gallery/detail/(?P<id>\d+)/$', detail_gallery, name='detail-gallery'),

    url(r'^association/$', association_information, name='association'),
]
