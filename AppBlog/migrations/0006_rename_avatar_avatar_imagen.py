# Generated by Django 4.0.4 on 2022-06-05 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0005_rename_imagen_avatar_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='avatar',
            new_name='imagen',
        ),
    ]
