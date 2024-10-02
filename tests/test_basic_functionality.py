import allure
from locators.order_feed_locators import OrderFeedLocators
from locators.main_page_locators import MainPageLocators
import urls


class TestBasicFinctionality:
    @allure.title('Переход по клику на "Конструктор"')
    def test_transition_tap_button_designer(self, main_page, order_feed_page):
        main_page.wait_element_invisibility_of_element(MainPageLocators.ELEMENT)
        main_page.click_button_order_feed()
        order_feed_page.wait_element_visibility_of_element(OrderFeedLocators.ORDER_FEED_TITLE)
        order_feed_page.click_button_designer()
        main_page.wait_element_visibility_of_element(MainPageLocators.MAIN_PAGE_TITLE)
        assert main_page.get_current_url() == urls.MAIN_PAGE

    @allure.title('Переход по клику на "Лента заказов"')
    def test_transition_tap_button_oder_feed(self, main_page):
        main_page.wait_element_invisibility_of_element(MainPageLocators.ELEMENT)
        main_page.click_button_order_feed()
        assert main_page.get_current_url() == urls.ORDER_FEED

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_apper_window(self, main_page):
        main_page.wait_element_invisibility_of_element(MainPageLocators.ELEMENT)
        main_page.click_for_ingredient()
        assert main_page.find_element(MainPageLocators.INGREDIENT_DETAILS)

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_window_ingredient_close_tap_cross(self, main_page):
        main_page.wait_element_invisibility_of_element(MainPageLocators.ELEMENT)
        main_page.click_for_ingredient()
        main_page.wait_element_visibility_of_element(MainPageLocators.CROSS_WINDOW_IGREDIENT)
        main_page.close_window_igredient()
        main_page.wait_element_visibility_of_element(MainPageLocators.MAIN_PAGE_TITLE)
        assert main_page.find_element(MainPageLocators.MAIN_PAGE_TITLE)

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_count_ingredients(self, main_page):
        main_page.wait_element_invisibility_of_element(MainPageLocators.ELEMENT)
        main_page.drag_and_drop_buns()
        assert main_page.get_counter_ingredient() == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_login_user_success_making_an_order(self, personal_account, main_page):
        main_page.wait_element_invisibility_of_element(MainPageLocators.ELEMENT)
        main_page.drag_and_drop_souse()
        main_page.click_button_making_an_order()
        main_page.wait_element_element_to_be_clickable(MainPageLocators.BUTTON_CLOSE_WINDOW_IDENTIFICATION_ORDER)
        assert main_page.find_element(MainPageLocators.IDENTIFICATION_ORDER)
