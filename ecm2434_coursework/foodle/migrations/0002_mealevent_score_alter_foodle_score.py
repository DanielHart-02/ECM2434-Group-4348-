# Generated by Django 5.0.2 on 2024-02-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealevent',
            name='score',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='foodle',
            name='score',
            field=models.PositiveBigIntegerField(),
        ),
    ]
