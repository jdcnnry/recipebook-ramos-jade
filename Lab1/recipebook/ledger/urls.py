from django.urls import path
from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('list/', RecipeListView.as_view(), name='list'),
    path('<int:pk>', RecipeDetailView.as_view(), name='recipe-detail')
]

app_name = "ledger"