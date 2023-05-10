import os
from django.views.generic import ListView

from utils.pagination import make_pagination
from recipes.models import Recipe

PER_PAGE = int(os.environ.get('PER_PAGE', 1))


class RecipeListViewBase(ListView):
    model = Recipe
    context_object_name = 'recipes'
    ordering = ['-id']
    template_name = 'recipes/pages/home.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            is_published=True,
        )

        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        page_obj, pagination_range = make_pagination(
            self.request,
            ctx.get('recipes'),
            PER_PAGE,
        )

        ctx.update(
            {'recipes': page_obj, 'pagination_range': pagination_range}
        )
        return ctx
