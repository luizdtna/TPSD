# Generated by Django 3.1.3 on 2020-11-23 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processos', '0022_auto_20201123_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiOA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ciclo_De_Vida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ciclo_De_Vida', to='processos.ciclo_de_vida')),
                ('Geral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Geral', to='processos.geral')),
                ('Tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tecnico', to='processos.tecnico')),
            ],
        ),
    ]
