# Generated by Django 4.0.5 on 2022-08-06 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_producto_compradop_alter_catalogo_enlace_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catalogo',
            new_name='Categoria',
        ),
    ]