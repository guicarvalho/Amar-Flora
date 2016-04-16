from django.conf.urls import url

from core.views import home, go_gallery


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'gallery/$', go_gallery, name='gallery'),
]
