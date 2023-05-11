from django.contrib import admin
from .models import User, VerifyPhone, Region, District
from modeltranslation.admin import TranslationAdmin


# @admin.register(Region)
# class RegAdmin(TranslationAdmin):
#     pass
#
#
# @admin.register(District)
# class DistrictAdmin(TranslationAdmin):
#     pass


admin.site.register(User)
admin.site.register(VerifyPhone)
