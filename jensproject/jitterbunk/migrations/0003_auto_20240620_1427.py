# Generated by Django 3.2 on 2024-06-20 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jitterbunk', '0002_bunkform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bunkform',
            old_name='from_user',
            new_name='bunked',
        ),
        migrations.RenameField(
            model_name='bunkform',
            old_name='to_user',
            new_name='bunker',
        ),
    ]
