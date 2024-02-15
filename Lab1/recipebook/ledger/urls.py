from django.urls import path
from .views import index, recipe_list, recipe_1, recipe_2

urlpatterns = [
    path('', index, name='index'),
    path('list/', recipe_list, name='list'),
    path('1/', recipe_1, name='list'),
    path('2/', recipe_2, name='list'),
]

app_name = "ledger"