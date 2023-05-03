import time

from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from utils.browser import make_chrome_browser


class RecipeBaseFunctionalTest(LiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=5):
        time.sleep(seconds)


class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):
    def test_recipe_home_page_without_recipes_not_found_message(self):
        self.browser.get(self.live_server_url)
        # self.sleep(2)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('No recipes found here :(', body.text)
