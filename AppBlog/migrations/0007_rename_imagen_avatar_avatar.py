# Generated by Django 4.0.4 on 2022-06-05 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0006_rename_avatar_avatar_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='imagen',
            new_name='avatar',
        ),
    ]
