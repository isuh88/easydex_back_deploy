# Generated by Django 4.2.3 on 2023-07-12 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='dex',
        ),
    ]
