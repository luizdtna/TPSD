# Generated by Django 3.1.3 on 2020-11-14 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processos', '0006_auto_20201114_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geral',
            name='tamanho',
            field=models.IntegerField(blank=True, default=88, null=True),
        ),
    ]
