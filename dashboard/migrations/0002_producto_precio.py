# Generated by Django 5.0.1 on 2024-01-14 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
