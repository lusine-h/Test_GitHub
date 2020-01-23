import unittest
from Webdriver import Driver
from Values import strings
from pageobjects.github_page import GitHubPage
import time


class TestGitHub(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_sign_in_with_correct_username_and_password(self):
        page = GitHubPage(self.driver)
        page.choose_sign_in()
        time.sleep(2)
        page.input_email_address(strings.correct_email_address)
        page.input_password(strings.correct_password)
        page.validate_account_is_opened()

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == "__main__":
    unittest.main()

