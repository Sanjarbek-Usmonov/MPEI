from django.db import models
from django.utils.translation import gettext_lazy as _

class SiteLogo(models.Model):
    logo_name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('Sayt logotipi (nom)'))
    logo_image = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name=_('Sayt logotipi (rasm)'))

    class Meta:
        verbose_name = _('Site logo')
        verbose_name_plural = _('Site logo')

class IntroSection(models.Model):
    title = models.CharField(max_length=255, null=True, verbose_name=_('Title'))
    some_text = models.TextField(null=True, verbose_name=_('Some text'))
    image = models.ImageField(upload_to='images', null=True, verbose_name=_('Image'))

    class Meta:
        verbose_name = _('Introduction section')
        verbose_name_plural = _('Introduction section')

class SocialLinks(models.Model):
    instagram = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Instagram link'))
    facebook = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Facebook link'))
    youtube = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Youtube link'))
    twitter = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Twitter link'))
    linkedin = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('LinkedIn link'))
    telegram = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Telegram link'))
    whatsapp = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Whatsapp link'))

    class Meta:
        verbose_name = _("Social Links")
        verbose_name_plural = _("Social Links")