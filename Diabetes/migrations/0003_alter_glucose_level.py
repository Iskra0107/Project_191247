# Generated by Django 4.0.5 on 2022-09-02 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diabetes', '0002_myuser_glucose_myusers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glucose',
            name='level',
            field=models.CharField(max_length=20),
        ),
    ]
