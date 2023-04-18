from django.urls import path
from recipes import views

app_name = "recipes"

urlpatterns = [
    path("recipes/category/<int:category_id>/", views.category,
         name="category"),
    path("", views.home, name="home"),
    path("recipes/<int:id>/", views.recipe, name="recipe"),
    path("recipes/search/", lambda request: ..., name="search"),
]
