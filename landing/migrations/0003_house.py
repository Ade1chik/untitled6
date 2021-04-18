# Generated by Django 3.1a1 on 2020-05-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20200326_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('har', models.CharField(max_length=64)),
                ('http', models.URLField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]