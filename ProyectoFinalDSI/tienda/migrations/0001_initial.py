# Generated by Django 4.0.5 on 2022-07-24 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('idnumcat', models.AutoField(default=1, primary_key=True, serialize=False, verbose_name='Id de la categoría')),
                ('titulo', models.CharField(max_length=200, verbose_name='Nombre de la categoría')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('imagen', models.ImageField(upload_to='ProyectosImagenes', verbose_name='Imagen de la categoría')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha agregado')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Fecha de última actualización')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['-creado'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idnumprod', models.IntegerField(default=1, primary_key=True, serialize=False, verbose_name='Id del producto')),
                ('cantidadp', models.IntegerField(default=1, verbose_name='Cantidad disponible')),
                ('nombrep', models.CharField(max_length=200, verbose_name='Nombre del producto')),
                ('detallep', models.TextField(verbose_name='Descripción')),
                ('marcap', models.CharField(max_length=100, verbose_name='Marca del dispositivo')),
                ('preciop', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('imagenp', models.ImageField(upload_to='ProyectosImagenes', verbose_name='Imagen del producto')),
                ('agregadop', models.DateTimeField(auto_now_add=True, verbose_name='Fecha agregado')),
                ('modificadop', models.DateTimeField(auto_now=True, verbose_name='Fecha de última modificación')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['-agregadop'],
            },
        ),
    ]
