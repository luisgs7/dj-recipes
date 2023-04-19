from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeHomeViewTest(RecipeTestBase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('<h1>No recipes found here :(</h1>',
                      response.content.decode('utf-8'))
        # A função decode é para converter de bytes para string

    def test_recipe_home_template_loads_recipes(self):
        #TODO Criando uma nova receita a partir da classe RecipeTestBase # noqa disable=E265
        self.make_recipe(category_data={'name': 'café da manhã'})

        response = self.client.get(reverse('recipes:home'))
        #TODO Esta função permite buscar os dados do html(Do template) # noqa disable=E265
        content = response.content.decode('utf-8')

        self.assertIn('Recipe Title', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 Porções', content)
        self.assertIn('café da manhã', content)

        #TODO Buscar os dados a partir do context da view, antes de serem enviados ao template  # noqa disable=E265
        context = response.context['recipes']

        self.assertEqual(len(context), 1)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        """Test recipe is_published False dont show"""
        # Need a recipe for this test
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))

        # Check is not recipe exists
        self.assertIn(
            '<h1>No recipes found here :(</h1>',
            response.content.decode('utf-8')
        )
