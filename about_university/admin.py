from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

admin.site.register(LegalInfo)
admin.site.register(WEBresource)
admin.site.register(Partners)
admin.site.register(Honorary)

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(CustomUser, UserAdmin)

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

@admin.register(IntroduceMEI)
class IntroduceMEIAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'subject', 'created_at']
    search_fields = ['fullname', 'id', 'subject']

