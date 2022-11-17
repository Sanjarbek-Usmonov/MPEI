from modeltranslation import translator
from . import models

@translator.register(models.IntroduceMEI)
class IntroduceMEITranslation(translator.TranslationOptions):
    fields = ('text',)