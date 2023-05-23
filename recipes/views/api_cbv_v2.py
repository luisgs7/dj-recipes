from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

from recipes.models import Recipe
from recipes.serializers import (
    RecipeSerializer,
)


class RecipeAPIv2Pagination(PageNumberPagination):
    page_size = 3


class RecipeAPIv2List(ListCreateAPIView):
    queryset = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIv2Pagination
