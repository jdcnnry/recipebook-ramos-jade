from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[self.pk])


class RecipeIngredient(models.Model):
    qty = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE,
        related_name='recipe'
    )
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
        related_name='ingredients'
    )

    def __str__(self):
        return '{} of {}' .format(self.qty, self.ingredient)