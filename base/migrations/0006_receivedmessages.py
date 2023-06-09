# Generated by Django 4.1.3 on 2022-12-01 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_joinournewsletterform_joinournewslettertext'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceivedMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, null=True, verbose_name='email')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Received messages',
                'verbose_name_plural': 'Received messages',
            },
        ),
    ]
