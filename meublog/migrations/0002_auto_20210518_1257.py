# Generated by Django 3.1.7 on 2021-05-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meublog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='ativo',
            field=models.BooleanField(choices=[(True, 'Ativo'), (False, 'Desativo')], default=True),
        ),
    ]
