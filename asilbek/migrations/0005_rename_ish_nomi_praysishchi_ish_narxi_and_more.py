# Generated by Django 5.0 on 2023-12-18 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asilbek', '0004_maxsulot_praysishchi_prayszakaz_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='praysishchi',
            old_name='ish_nomi',
            new_name='ish_narxi',
        ),
        migrations.RenameField(
            model_name='prayszakaz',
            old_name='ish_nomi',
            new_name='ish_narxi',
        ),
    ]