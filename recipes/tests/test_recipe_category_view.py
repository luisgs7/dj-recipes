from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeCategoryViewTest(RecipeTestBase):
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func.view_class, views.RecipeListViewCategory)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        #TODO Criando uma nova receita a partir da classe RecipeTestBase # noqa disable=E265
        needed_title = 'This is a category test'
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:category', kwargs={
            'category_id': 1,
        }))
        #TODO Esta função permite buscar os dados do html(Do template) # noqa disable=E265
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 Porções', content)

    def test_recipe_category_template_dont_load_recipes_not_published(self):
        """Test recipe is_published False dont show"""
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:recipe', kwargs={
            'pk': recipe.category.pk
        }))

        self.assertEqual(response.status_code, 404)
