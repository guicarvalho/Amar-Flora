# coding: utf-8

from django.contrib import admin

from core.models import (Associate, News, Partner, Member,
                         Classified, Request, Gallery, Association_information,
                         UsefulPhone, ImageNews, ImageClassified, Document)


class AssociateAdmin(admin.ModelAdmin):
    pass


class NewsAdmin(admin.ModelAdmin):
    pass


class PartnerAdmin(admin.ModelAdmin):
    pass


class ClassifiedAdmin(admin.ModelAdmin):
    pass


class RequestAdmin(admin.ModelAdmin):
    pass


class MemberAdmin(admin.ModelAdmin):
    pass


class GalleryAdmin(admin.ModelAdmin):
    pass


class AssociationInformationAdmin(admin.ModelAdmin):
	pass


class UsefulPhoneAdmin(admin.ModelAdmin):
	pass


class ImageNewsAdmin(admin.ModelAdmin):
    pass


class ImageClassifiedAdmin(admin.ModelAdmin):
    pass


class DocumentAdmin(admin.ModelAdmin):
    pass



admin.site.register(Associate, AssociateAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Classified, ClassifiedAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Association_information, AssociationInformationAdmin)
admin.site.register(UsefulPhone, UsefulPhoneAdmin)
admin.site.register(ImageNews, ImageNewsAdmin)
admin.site.register(ImageClassified, ImageClassifiedAdmin)
admin.site.register(Document, DocumentAdmin)
