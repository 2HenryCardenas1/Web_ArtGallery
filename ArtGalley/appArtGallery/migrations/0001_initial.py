# Generated by Django 3.2.3 on 2021-05-21 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('imagen', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pieza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pieza', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('small_descripcion', models.TextField()),
                ('big_descripcion', models.TextField()),
                ('imagen', models.CharField(max_length=255)),
                ('imagen2', models.CharField(max_length=255)),
                ('imagen4', models.ImageField(upload_to='')),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appArtGallery.artista')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appArtGallery.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Facturacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=250)),
                ('apellido_usuario', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('ciudad', models.CharField(max_length=300)),
                ('departamento', models.CharField(max_length=200)),
                ('codigo_postal', models.CharField(max_length=6)),
                ('pieza_id_pieza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appArtGallery.pieza')),
            ],
        ),
    ]
