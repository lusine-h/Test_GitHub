from selenium.webdriver.common.by import By
from TestData import values
from .basescreen import BaseScreen


class GitHubPage(BaseScreen):
    sign_in = (By.XPATH, '//a[@class="HeaderMenu-link no-underline mr-3"]')
    email_input = (By.ID, "login_field")
    password_input = (By.ID, "password")
    sign_in_button = (By.XPATH, '//input[@name="commit"]')
    username = (By.XPATH, '//strong[@class="css-truncate-target"]')
    element = (By.XPATH, '/html/body/div[1]/header/div[7]/details/summary')

    def choose_sign_in(self):
        self.wait_until_clickable(self.sign_in).click()

    def input_email_address(self, email_address):
        email_field = self.wait_until_clickable(self.email_input)
        email_field.send_keys(email_address)

    def input_password(self, psw):
        password_field = self.wait_until_clickable(self.password_input)
        password_field.send_keys(psw)
        self.wait_until_clickable(self.sign_in_button).click()

    def validate_account_is_opened(self):
        self.select_element(self.element).click()
        text = self.select_element(self.username).text
        assert text == values.user, " Incorrect email address or password"








