# Generated by Django 4.2 on 2024-12-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_privatemessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(),
        ),
    ]