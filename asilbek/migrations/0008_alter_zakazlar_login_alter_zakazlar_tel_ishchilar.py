# Generated by Django 4.1.7 on 2023-12-21 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asilbek', '0007_zakazlar_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zakazlar',
            name='login',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='zakazlar',
            name='tel',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.CreateModel(
            name='Ishchilar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=150)),
                ('tel', models.CharField(max_length=150)),
                ('kasb', models.ForeignKey(default='-----', max_length=150, on_delete=django.db.models.deletion.CASCADE, to='asilbek.maxsulot', to_field='maxsulot_nomi')),
            ],
        ),
    ]
