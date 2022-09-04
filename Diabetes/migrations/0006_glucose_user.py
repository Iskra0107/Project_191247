# Generated by Django 4.0.5 on 2022-09-02 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Diabetes', '0005_remove_glucose_myusers_glucose_myusers_glucoseuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='glucose',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
