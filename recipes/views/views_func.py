import os
from django.db.models import Q, F # noqa = F401
from django.db.models.aggregates import Count
from django.http import Http404
# from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404

from recipes.models import Recipe
from utils.pagination import make_pagination

PER_PAGE = int(os.environ.get('PER_PAGE', 6))


def home(request):
    recipes = Recipe.objects.filter(
              is_published=True,
              ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, "recipes/pages/home.html",
                  context={
                      'recipes': page_obj,
                      'pagination_range': pagination_range,
                  })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id'),
    )

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, "recipes/pages/home.html",
                  context={
                      "recipes": page_obj,
                      "pagination_range": pagination_range,
                      "title": f"{recipes[0].category.name} - Category"
                  })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(request, "recipes/pages/recipe-view.html",
                  context={
                    "recipe": recipe,
                    "is_detail_page": True,
                  })


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
            is_published=True
        )
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, "recipes/pages/search.html", {
        'page_title': f'Search for "{search_term} "',
        'search_term': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}',
    })


def theory(request):
    # recipes = Recipe.objects.all()
    # recipes = recipes.filter(title__icontains='Reci')
    # try:
    #     # O .get() levanta uma exceção, o filter NÃO
    #     recipes = Recipe.objects.get(pk=10000)
    # except ObjectDoesNotExist:
    #     recipes = None
    # recipes = Recipe.objects.filter(
    #     Q(
    #         Q(title__icontains='r', # noqa = E261  AND
    #           id__gt=2,  # AND
    #           is_published=True,) | # noqa = E261 OR
    #         Q(
    #           id__gt=1, # noqa = E261 Maior que > 1
    #          )
    #     )
    # )[:10] # noqa = E261 LIMIT = 10

    # recipes = Recipe.objects.filter(
    #      id=F('author__id'),
    # ).order_by('-id', 'title')[:1]

    # recipes = Recipe.objects.values(
    #     'id', 'title', 'author__username',
    # )[:10]

    # O .only() busca somente os citados, se houver outros dados, se
    # preciso ele realiza consultas redundantes
    # recipes = Recipe.objects.only(
    #     'id', 'title', 'author__username',
    # )

    # O .defer(), busca todos os dados, com exceção do que foi passado, se
    # preciso
    # ele busca os dados, se tornando extremamente lento.
    # recipes = Recipe.objects.defer(
    #     'id', 'title', 'author__username',
    # )
    recipes = Recipe.objects.values('id', 'title')[:5]
    number_of_recipes = recipes.aggregate(number=Count('id'))

    context = {
        'recipes': recipes,
        'number_of_recipes': number_of_recipes,
    }

    return render(
        request,
        'recipes/pages/theory.html',
        context,
    )
