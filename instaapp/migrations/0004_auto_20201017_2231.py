# Generated by Django 3.1.2 on 2020-10-17 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0003_auto_20201017_2230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='user',
            new_name='profile',
        ),
    ]