from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

from tag.models import Tag
from recipes.models import Recipe
from recipes.serializers import (
    RecipeSerializer,
    TagSerializer,
)


class RecipeAPIv2Pagination(PageNumberPagination):
    page_size = 3


class RecipeAPIv2List(ListCreateAPIView):
    queryset = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIv2Pagination
