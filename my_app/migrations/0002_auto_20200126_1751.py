# Generated by Django 3.0.2 on 2020-01-26 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='search',
            options={'verbose_name_plural': 'Searches'},
        ),
        migrations.AlterField(
            model_name='search',
            name='search',
            field=models.CharField(max_length=500),
        ),
    ]
