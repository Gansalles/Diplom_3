import allure

from pages.base_page import BasePage
from locators.recovery_password_page_locators import RecoveryPasswordPageLocators


class RecoveryPasswordPage(BasePage):
    @allure.step('Заполняем поле Email')
    def enter_email(self, email):
        self.send_keys(RecoveryPasswordPageLocators.PLACEHOLDER_EMAIL, email)

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def click_button_recovery(self):
        self.click_element(RecoveryPasswordPageLocators.BUTTON_RECOVERY)
