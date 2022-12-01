from modeltranslation import translator
from . import models

@translator.register(models.SiteLogo)
class SiteLogoTranslation(translator.TranslationOptions):
    fields = ('logo_name',)

@translator.register(models.IntroSection)
class IntroSectionTranslation(translator.TranslationOptions):
    fields = ('title', 'some_text')

@translator.register(models.ContactAddress)
class ContactAddressTranslation(translator.TranslationOptions):
    fields = ('address',)

@translator.register(models.JoinOurNewsletterText)
class JoinOurNewsletterTextTranslation(translator.TranslationOptions):
    fields = ('text',)
