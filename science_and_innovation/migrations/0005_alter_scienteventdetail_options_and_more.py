# Generated by Django 4.1.3 on 2022-12-04 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('science_and_innovation', '0004_journals_text_oz_researchanddev_text_oz_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scienteventdetail',
            options={'verbose_name': 'Scientific event detail', 'verbose_name_plural': 'Scientific event detail'},
        ),
        migrations.AlterModelOptions(
            name='scientevents',
            options={'verbose_name': 'Scientific events', 'verbose_name_plural': 'Scientific events'},
        ),
    ]
