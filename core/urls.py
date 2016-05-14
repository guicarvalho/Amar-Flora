from django.conf.urls import url

from core.views import (home, list_associate, new_associate,
					   list_news, list_partner, list_classified,
					   new_request)


urlpatterns = [
    url(r'^$', home, name='home'),

    url(r'^associate/$', list_associate, name='associate-list'),
    url(r'^associate/new/$', new_associate, name='associate-new'),
    
    url(r'^news/$', list_news, name='news-list'),

    url(r'^partner/$', list_partner, name='partner-list'),
    
    url(r'^classified/$', list_classified, name='classified-list'),

    url(r'^request/new/$', new_request, name='request-new'),

]
