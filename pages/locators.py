from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM_LINK = (By.ID, 'login_form')
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, 'register_form')


class ProductPageLocators:
    ADD_TO_BASKET = (By.XPATH, ".//*[@class='btn btn-lg btn-primary btn-add-to-basket']")
    BOOK_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    BOOK_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    BASKET_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    ADDED_BOOK_NAME = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')