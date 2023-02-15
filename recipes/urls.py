from django.urls import path, include
from recipes import views


urlpatterns = [
    path("", views.home),
    path("recipes/<int:id>/", views.recipe)
]