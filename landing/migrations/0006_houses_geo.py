# Generated by Django 3.1a1 on 2020-05-26 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_houses_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='houses',
            name='geo',
            field=models.CharField(default='Местоположение не указано', max_length=64),
        ),
    ]
