# Generated by Django 3.2.3 on 2021-06-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhello', '0008_auto_20210613_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='account',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='personal',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]