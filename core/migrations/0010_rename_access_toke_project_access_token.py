# Generated by Django 5.1.4 on 2025-04-06 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_project_access_toke'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='access_toke',
            new_name='access_token',
        ),
    ]
