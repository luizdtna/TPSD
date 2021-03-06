# Generated by Django 3.1.3 on 2020-11-20 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processos', '0014_auto_20201120_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agregacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agregacao', models.CharField(blank=True, default='nulo', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cobertura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cobertura', models.CharField(blank=True, default='nulo', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Descricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, default='nulo', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entrada_do_catalogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalogo', models.CharField(blank=True, default='nulo', max_length=255, null=True)),
                ('entrada', models.CharField(blank=True, default='nulo', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estrutura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estrutura', models.CharField(blank=True, default='nulo', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(blank=True, default='nulo', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Palavras_chave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palavras_chaves', models.CharField(blank=True, default='nulo', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Titulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, default='nulo', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Geral2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Agregacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Agregacao', to='processos.agregacao')),
                ('Cobertura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cobertura', to='processos.cobertura')),
                ('Descricao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Descricao', to='processos.descricao')),
                ('Entrada_do_catalogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processos.entrada_do_catalogo')),
                ('Estrutura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Estrutura', to='processos.estrutura')),
                ('Idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Idioma', to='processos.idioma')),
                ('Palavras_chave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Palavras_chave', to='processos.palavras_chave')),
                ('Titulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Titulo', to='processos.titulo')),
            ],
        ),
    ]
