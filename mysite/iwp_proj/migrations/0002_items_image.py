# Generated by Django 3.1 on 2020-08-25 08:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('iwp_proj', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='profile_image'),
            preserve_default=False,
        ),
    ]
