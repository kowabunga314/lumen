# Generated by Django 3.2.5 on 2021-07-28 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0004_auto_20210727_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='url',
        ),
        migrations.RemoveField(
            model_name='series',
            name='thumbnail_url',
        ),
        migrations.AddField(
            model_name='photo',
            name='photo',
            field=models.ImageField(default='images/placeholder.jpeg', upload_to='images'),
        ),
        migrations.AddField(
            model_name='series',
            name='thumbnail',
            field=models.ImageField(default='images/placeholder.jpeg', upload_to='images'),
        ),
    ]
