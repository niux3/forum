# Generated by Django 4.2 on 2024-12-18 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_privatemessage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PrivateMessage',
        ),
    ]