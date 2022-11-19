from modeltranslation import translator
from . import models

@translator.register(models.ResearchAndDev)
class IntroduceMEITranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.ScientInfrastructure)
class IntroduceMEITranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.ScientificCert)
class IntroduceMEITranslation(translator.TranslationOptions):
    fields = ('name',)

@translator.register(models.Journals)
class IntroduceMEITranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.ScientEvents)
class IntroduceMEITranslation(translator.TranslationOptions):
    fields = ('name',)

@translator.register(models.ScientEventDetail)
class IntroduceMEITranslation(translator.TranslationOptions):
    fields = ('text',)