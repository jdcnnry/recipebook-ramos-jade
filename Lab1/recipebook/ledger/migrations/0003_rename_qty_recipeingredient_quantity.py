# Generated by Django 5.0.2 on 2024-03-15 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_recipe_author_recipe_created_on_recipe_updated_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipeingredient',
            old_name='qty',
            new_name='quantity',
        ),
    ]