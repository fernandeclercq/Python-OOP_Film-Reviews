# Generated by Django 4.1.2 on 2022-11-06 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='opnieuwBebijken',
            new_name='opnieuwBekijken',
        ),
    ]
