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

admin.site.register(Schedule)

@admin.register(Faculty)
class IntroduceMEIAdmin(MyTranslationAdmin):
    list_display = ['id', 'name']
    search_fields = ['name', 'id']

@admin.register(Group)
class IntroduceMEIAdmin(MyTranslationAdmin):
    list_display = ['id', 'name']
    search_fields = ['name', 'id']

@admin.register(EduProgram)
class IntroduceMEIAdmin(MyTranslationAdmin):
    list_display = ['id', 'text']
    search_fields = ['text', 'id']

@admin.register(TreResults)
class IntroduceMEIAdmin(MyTranslationAdmin):
    list_display = ['id', 'text']
    search_fields = ['text', 'id']

@admin.register(AdditionalEdu)
class IntroduceMEIAdmin(MyTranslationAdmin):
    list_display = ['id', 'text']
    search_fields = ['text', 'id']

@admin.register(DistanceEdu)
class IntroduceMEIAdmin(MyTranslationAdmin):
    list_display = ['id', 'text']
    search_fields = ['text', 'id']

@admin.register(EmpAndInternship)
class IntroduceMEIAdmin(MyTranslationAdmin):
    list_display = ['id', 'text']
    search_fields = ['text', 'id']

@admin.register(FinalQua)
class IntroduceMEIAdmin(MyTranslationAdmin):
    list_display = ['id', 'text']
    search_fields = ['text', 'id']

@admin.register(OfficialDocs)
class IntroduceMEIAdmin(MyTranslationAdmin):
    list_display = ['id', 'text']
    search_fields = ['text', 'id']