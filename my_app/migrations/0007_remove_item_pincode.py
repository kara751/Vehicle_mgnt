# Generated by Django 3.2.5 on 2021-10-28 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_auto_20211029_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='pincode',
        ),
    ]
