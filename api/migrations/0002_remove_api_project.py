# Generated by Django 2.1.1 on 2021-07-21 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='api',
            name='project',
        ),
    ]