# Generated by Django 4.0.4 on 2022-06-06 02:07

import AppBlog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0009_rename_imagen_restaurante_imagen_restaurante_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=AppBlog.models.filepath),
        ),
    ]
