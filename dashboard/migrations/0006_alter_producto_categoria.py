# Generated by Django 5.0.1 on 2024-02-24 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_producto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('Electrónicos', 'Electrónicos'), ('Muebles', 'Muebles'), ('Electrodomésticos', 'Electrodomésticos'), ('Limpieza', 'Limpieza'), ('Comestibles', 'Comestibles')], max_length=100, null=True),
        ),
    ]
