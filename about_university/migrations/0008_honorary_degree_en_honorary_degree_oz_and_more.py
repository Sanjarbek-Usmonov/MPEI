# Generated by Django 4.1.3 on 2022-12-03 16:09

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_university', '0007_delete_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='honorary',
            name='degree_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Degree'),
        ),
        migrations.AddField(
            model_name='honorary',
            name='degree_oz',
            field=models.CharField(max_length=200, null=True, verbose_name='Degree'),
        ),
        migrations.AddField(
            model_name='honorary',
            name='degree_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Degree'),
        ),
        migrations.AddField(
            model_name='honorary',
            name='degree_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='Degree'),
        ),
        migrations.AddField(
            model_name='honorary',
            name='fullname_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Full name'),
        ),
        migrations.AddField(
            model_name='honorary',
            name='fullname_oz',
            field=models.CharField(max_length=150, null=True, verbose_name='Full name'),
        ),
        migrations.AddField(
            model_name='honorary',
            name='fullname_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Full name'),
        ),
        migrations.AddField(
            model_name='honorary',
            name='fullname_uz',
            field=models.CharField(max_length=150, null=True, verbose_name='Full name'),
        ),
        migrations.AddField(
            model_name='legalinfo',
            name='text_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='legalinfo',
            name='text_oz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='legalinfo',
            name='text_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='legalinfo',
            name='text_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='partners',
            name='text_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='partners',
            name='text_oz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='partners',
            name='text_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='partners',
            name='text_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='webresource',
            name='text_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='webresource',
            name='text_oz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='webresource',
            name='text_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='webresource',
            name='text_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
    ]