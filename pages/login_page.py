from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'Url is not login page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_LINK), 'Register form is not presented'

    def register_new_user(self, email: str, password: str):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_ADDRESS)
        reg_email.send_keys(email)
        reg_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        reg_password.send_keys(password)
        repeat_reg_password = self.browser.find_element(*LoginPageLocators.REGISTER_REPEAT_PASSWORD)
        repeat_reg_password.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)
        submit_button.click()
