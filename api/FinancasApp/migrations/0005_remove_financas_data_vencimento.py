# Generated by Django 4.2.7 on 2023-11-25 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FinancasApp', '0004_rename_financa_financas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financas',
            name='data_vencimento',
        ),
    ]
