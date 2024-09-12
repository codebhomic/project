# Generated by Django 5.1 on 2024-09-12 17:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pitch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('amount_requested', models.DecimalField(decimal_places=2, max_digits=10)),
                ('equity_offer', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('open', 'Open'), ('closed', 'Closed'), ('funded', 'Funded'), ('rejected', 'Rejected')], default='open', max_length=10)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pitches', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StartupDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilepic', models.ImageField(blank=True, default='startup/profilepics/useravatar.png', null=True, upload_to='startup/profilepics/')),
                ('startup_name', models.CharField(max_length=250)),
                ('startup_detail', models.TextField()),
                ('founder_name', models.CharField(max_length=250)),
                ('founder_detail', models.TextField()),
                ('co_founders', models.BooleanField(default=False)),
                ('co_founders_details', models.TextField(blank=True, null=True)),
                ('team', models.BooleanField(default=False)),
                ('team_details', models.TextField(blank=True, null=True)),
                ('business_model', models.TextField()),
                ('resume', models.FileField(blank=True, null=True, upload_to='static/startup/')),
                ('additional_details', models.FileField(blank=True, null=True, upload_to='static/startup/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
