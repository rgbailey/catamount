# Generated by Django 3.1.1 on 2020-09-16 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city_slug',
            field=models.CharField(max_length=50),
        ),
    ]
