# Generated by Django 4.0.5 on 2022-07-17 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_alter_producto_imagenp_alter_producto_nombrep'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogo',
            name='idnumcat',
            field=models.IntegerField(default=0, verbose_name='Nuevo número id del catálogo'),
        ),
        migrations.AddField(
            model_name='producto',
            name='idnumprod',
            field=models.IntegerField(default=0, verbose_name='Número id del catálogo al que será agregado'),
        ),
    ]
