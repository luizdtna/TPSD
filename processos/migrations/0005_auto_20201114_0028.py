# Generated by Django 3.1.3 on 2020-11-14 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processos', '0004_geral_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='geral',
            name='formato',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='geral',
            name='tamanho',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
