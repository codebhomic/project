# Generated by Django 5.1 on 2024-08-24 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_myuser_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='profile_pic',
        ),
    ]
