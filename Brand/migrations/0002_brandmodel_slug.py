# Generated by Django 5.0.6 on 2024-07-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
