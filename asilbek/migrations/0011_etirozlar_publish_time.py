# Generated by Django 4.1.7 on 2023-12-22 10:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('asilbek', '0010_etirozlar'),
    ]

    operations = [
        migrations.AddField(
            model_name='etirozlar',
            name='publish_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
