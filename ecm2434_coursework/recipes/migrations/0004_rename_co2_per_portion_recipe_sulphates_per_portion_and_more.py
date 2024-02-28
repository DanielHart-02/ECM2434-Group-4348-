# Generated by Django 5.0.2 on 2024-02-28 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_co2_per_portion_alter_recipe_prep_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='co2_per_portion',
            new_name='sulphates_per_portion',
        ),
        migrations.AlterField(
            model_name='ingredientrating',
            name='ingredient',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
