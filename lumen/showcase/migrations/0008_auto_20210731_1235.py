# Generated by Django 3.2.5 on 2021-07-31 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0007_alter_photo_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='photo',
            name='location',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, default='images/placeholder.jpeg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='series',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
