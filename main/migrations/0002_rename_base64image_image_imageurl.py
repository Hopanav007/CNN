# Generated by Django 3.2.6 on 2022-02-24 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='base64Image',
            new_name='imageUrl',
        ),
    ]
