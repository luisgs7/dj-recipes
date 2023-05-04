import pytest
from selenium.webdriver.common.by import By
from unittest.mock import patch

from .base import RecipeBaseFunctionalTest


@pytest.mark.functional_test
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):
    @patch('recipes.views.PER_PAGE', new=2)
    def test_recipe_home_page_without_recipes_not_found_message(self):
        # self.make_recipe_in_batch()
        self.browser.get(self.live_server_url)
        # self.sleep(2)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('No recipes found here :(', body.text)
