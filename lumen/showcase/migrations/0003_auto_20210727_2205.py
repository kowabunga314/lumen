# Generated by Django 3.2.5 on 2021-07-27 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0002_alter_series_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='series',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
