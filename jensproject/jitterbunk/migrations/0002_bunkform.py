# Generated by Django 3.2 on 2024-06-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jitterbunk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bunkform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.CharField(max_length=200)),
                ('to_user', models.CharField(max_length=200)),
            ],
        ),
    ]
