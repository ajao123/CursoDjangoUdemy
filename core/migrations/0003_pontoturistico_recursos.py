# Generated by Django 3.0.2 on 2020-01-29 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0001_initial'),
        ('core', '0002_auto_20200129_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='recursos',
            field=models.ManyToManyField(to='recursos.Recurso'),
        ),
    ]
