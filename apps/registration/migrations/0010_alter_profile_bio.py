# Generated by Django 4.2 on 2024-12-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_delete_privatemessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=8192),
        ),
    ]
