# Generated by Django 4.1.3 on 2022-11-19 14:28

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalEdu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Additional education',
                'verbose_name_plural': 'Additional education',
            },
        ),
        migrations.CreateModel(
            name='DistanceEdu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Distance education',
                'verbose_name_plural': 'Distance education',
            },
        ),
        migrations.CreateModel(
            name='EduProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Basic education programs',
                'verbose_name_plural': 'Basic education programs',
            },
        ),
        migrations.CreateModel(
            name='EmpAndInternship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Employment and internship',
                'verbose_name_plural': 'Employment and internship',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('name_uz', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Faculties',
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.CreateModel(
            name='FinalQua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Final qualifiers',
                'verbose_name_plural': 'Final qualifiers',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('name_uz', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.faculty', verbose_name='Faculties')),
            ],
            options={
                'verbose_name': 'Groups',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='OfficialDocs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Official documents',
                'verbose_name_plural': 'Official documents',
            },
        ),
        migrations.CreateModel(
            name='TreResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Training results',
                'verbose_name_plural': 'Training results',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.FileField(upload_to='files', verbose_name='Upload file')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.group', verbose_name='Groups')),
            ],
            options={
                'verbose_name': 'Schedule',
                'verbose_name_plural': 'Schedule',
            },
        ),
    ]
