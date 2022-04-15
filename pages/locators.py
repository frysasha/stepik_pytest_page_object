from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM_LINK = (By.ID, 'login_form')
    REGISTER_FORM_LINK = (By.ID, 'register_form')
    REGISTER_EMAIL_ADDRESS = (By.XPATH, '//*[@name="registration-email"]')
    REGISTER_PASSWORD = (By.XPATH, '//*[@name="registration-password1"]')
    REGISTER_REPEAT_PASSWORD = (By.XPATH, '//*[@name="registration-password2"]')
    REGISTER_SUBMIT_BUTTON = (By.XPATH, '//*[@name="registration_submit"]')


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div[1]')
    ADD_TO_BASKET = (By.XPATH, ".//*[@class='btn btn-lg btn-primary btn-add-to-basket']")
    BOOK_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    BOOK_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    BASKET_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    ADDED_BOOK_NAME = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini.pull-right.hidden-xs > span > a')


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.XPATH, '//*[@class="container-fluid page"]/div[1]/div[3]/div[2]/p')
    CONTENT_IN_BASKET = (By.CSS_SELECTOR, '#content_inner > div.basket-title.hidden-xs')
