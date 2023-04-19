from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeSearchViewTest(RecipeTestBase):
    def test_recipe_search_uses_correct_view_function(self):
        url = reverse('recipes:search')
        resolved = resolve(url)
        self.assertIs(resolved.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search')+'?q=react')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raise_404_if_no_search_term(self):
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        term = '?q=<Teste>'
        result = 'Search for &quot;&lt;Teste&gt; &quot;'

        url = reverse('recipes:search') + term
        response = self.client.get(url)
        self.assertIn(
            result,
            response.content.decode('utf-8'),
        )
