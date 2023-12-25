# Generated by Django 4.1.7 on 2023-12-24 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asilbek', '0015_savdotarixi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maxsulot',
            name='foiz',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='maxsulot',
            name='foiz_narxi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='maxsulot',
            name='narxi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='maxsulot',
            name='soni',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='praysishchi',
            name='ish_narxi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prayszakaz',
            name='ish_narxi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='savdotarixi',
            name='maxsulot_narxi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='savdotarixi',
            name='maxsulot_soni',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='xodimlar',
            name='oylik',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]