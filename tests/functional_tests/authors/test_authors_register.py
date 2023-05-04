import pytest

from .base import AuthorsBaseTest


@pytest.mark.functional_test
class AuthorsRegister(AuthorsBaseTest):
    def test_the_test(self):
        self.browser.get(self.live_server_url + '/authors/register')
        # self.sleep()
