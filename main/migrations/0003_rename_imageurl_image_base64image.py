# Generated by Django 3.2.6 on 2022-03-03 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_base64image_image_imageurl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='imageUrl',
            new_name='base64Image',
        ),
    ]
