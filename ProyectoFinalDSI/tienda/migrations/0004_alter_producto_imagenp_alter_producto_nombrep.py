# Generated by Django 4.0.5 on 2022-07-17 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_producto_alter_catalogo_creado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagenp',
            field=models.ImageField(upload_to='ProyectosImagenes', verbose_name='Imagen del producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombrep',
            field=models.CharField(max_length=200, verbose_name='Nombre del producto'),
        ),
    ]
