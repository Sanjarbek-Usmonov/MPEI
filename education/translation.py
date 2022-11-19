from modeltranslation import translator
from . import models

@translator.register(models.Faculty)
class IntroduceMEITranslation(translator.TranslationOptions):
    fields = ('name',)

@translator.register(models.Group)
class IntroduceMEITranslation(translator.TranslationOptions):
    fields = ('name',)

@translator.register(models.EduProgram)
class IntroduceMEITranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.TreResults)
class IntroduceMEITranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.AdditionalEdu)
class IntroduceMEITranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.DistanceEdu)
class IntroduceMEITranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.EmpAndInternship)
class IntroduceMEITranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.FinalQua)
class IntroduceMEITranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.OfficialDocs)
class IntroduceMEITranslation(translator.TranslationOptions):
    fields = ('text',)

