# Generated by Django 3.1.2 on 2020-12-01 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='profiles',
            new_name='profile',
        ),
    ]