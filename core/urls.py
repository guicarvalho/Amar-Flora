from django.conf.urls import url

from core.views import home, list_associate, new_associate, list_news


urlpatterns = [
    url(r'^$', home, name='home'),

    url(r'^associate/$', list_associate, name='associate-list'),
    url(r'^associate/new/$', new_associate, name='associate-new'),
    
    url(r'^news/$', list_news, name='news-list'),
]
