# coding: utf-8


from django.contrib import admin

from core.models import News


class NewsAdmin(admin.ModelAdmin):
	pass


admin.site.register(News, NewsAdmin)
