# Generated by Django 3.2.6 on 2021-08-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='banner',
            field=models.ImageField(blank=True, default='banners/default.png', upload_to='banners/'),
        ),
        migrations.AlterField(
            model_name='store',
            name='profile_pic',
            field=models.ImageField(blank=True, default='banners/default.png', upload_to='profiles/'),
        ),
    ]
