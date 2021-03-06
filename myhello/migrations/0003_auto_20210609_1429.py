# Generated by Django 3.2.3 on 2021-06-09 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhello', '0002_remove_contact_csex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('photo', models.URLField(blank=True)),
                ('location', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='contact',
        ),
    ]
