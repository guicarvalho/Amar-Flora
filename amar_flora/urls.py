# coding: utf-8

from django.conf.urls import url, include

from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^amar-flora/', include('core.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
