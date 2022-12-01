from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _

class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(SiteLogo)
class Site_LogoAdmin(MyTranslationAdmin):
    list_display = ['id', 'logo_name']
    search_fields = ['logo_name', 'id']

@admin.register(IntroSection)
class IntroSectionAdmin(MyTranslationAdmin):
    list_display = ['id', 'title']
    search_fields = ['title', 'id']

@admin.register(SocialLinks)
class IntroSectionAdmin(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ['id']

@admin.register(ContactAddress)
class ContactAddressAdmin(MyTranslationAdmin):
    list_display = ['id', 'phone_number']
    search_fields = ['id', 'phone_number']

@admin.register(JoinOurNewsletterText)
class JoinOurNewsletterTextAdmin(MyTranslationAdmin):
    list_display = ['id', 'text']

@admin.register(JoinOurNewsletterForm)
class JoinOurNewsletterFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']

@admin.register(ReceivedMessages)
class ReceivedMessagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']