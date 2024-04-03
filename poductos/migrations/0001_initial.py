# Generated by Django 5.0.2 on 2024-02-27 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('Id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=50)),
                ('esta_activa', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('Id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('producto', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, max_length=500, null=True)),
                ('precio', models.FloatField(default=0.0)),
                ('existencia', models.FloatField(default=0.0)),
                ('esta_activo', models.BooleanField(default=True)),
            ],
        ),
    ]