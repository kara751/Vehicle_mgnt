# Generated by Django 3.2.5 on 2021-10-28 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='capacity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='add',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
