from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

class IntroduceMEI(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Introducing with MPEI")
        verbose_name_plural = _("Introducing with MPEI")

class Contact(models.Model):
    fullname = models.CharField(max_length=150, null=True)
    subject = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=200, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class LegalInfo(models.Model):
    text = RichTextUploadingField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class WEBresource(models.Model):
    text = RichTextUploadingField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Partners(models.Model):
    text = RichTextUploadingField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Honorary(models.Model):
    fullname = models.CharField(max_length=150)
    degree = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

