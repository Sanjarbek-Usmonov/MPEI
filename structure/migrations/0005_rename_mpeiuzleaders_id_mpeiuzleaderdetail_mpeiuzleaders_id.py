# Generated by Django 4.1.3 on 2022-12-05 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0004_mpeiuzleaders_email_mpeiuzleaders_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mpeiuzleaderdetail',
            old_name='MPEIuzLeaders_id',
            new_name='mpeiuzLeaders_id',
        ),
    ]