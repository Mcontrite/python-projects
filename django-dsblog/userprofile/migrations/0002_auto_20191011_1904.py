# Generated by Django 2.2.4 on 2019-10-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='user/%Y%m%d/'),
        ),
    ]