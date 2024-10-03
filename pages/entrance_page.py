import urls
from locators.entrance_page_locators import EntrancePageLocators
from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators


class EntrancePage(BasePage):
    @allure.step('Открываем страницу входа в аккаунт')
    def open_entrance_page(self):
        self.open_url(f'{urls.BASE_PAGE}{urls.ENDPOINT_ENTRANCE_PAGE}')
        self.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
        self.wait_element_visibility_of_element(10, EntrancePageLocators.TITLE_ENTRANCE)

    @allure.step('Заполняем поле email')
    def enter_email_entrance_page(self, email):
        self.send_keys(EntrancePageLocators.PLACEHOLDER_EMAIL, email)

    @allure.step('Заполняем поле пароль')
    def enter_password_entrance_page(self, password):
        self.send_keys(EntrancePageLocators.PLACEHOLDER_PASSWORD, password)

    @allure.step('Нажимаем на кнопку восстановить пароль')
    def click_button_recovery_password(self):
        self.click_element(EntrancePageLocators.BUTTON_PASSWORD_RECOVERY)

    @allure.step('Нажимаем на кнопку "Вход"')
    def click_button_entrance(self):
        self.click_element(EntrancePageLocators.BUTTON_ENTER)
