from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ('name', 'author', 'created_on', 'updated_on')


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)