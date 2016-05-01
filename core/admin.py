# coding: utf-8


from django.contrib import admin

from core.models import News, Partner, Classified, Request


class NewsAdmin(admin.ModelAdmin):
	pass


class PartnerAdmin(admin.ModelAdmin):
	pass


class ClassifiedAdmin(admin.ModelAdmin):
	pass


class RequestAdmin(admin.ModelAdmin):
	pass


admin.site.register(News, NewsAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Classified, ClassifiedAdmin)
admin.site.register(Request, RequestAdmin)
