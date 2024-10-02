from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED_TITLE = (By.XPATH, ".//h1[text() = 'Лента заказов']")
    ORDER = (By.XPATH, './/div[contains(@class, "contentBox")]/ul[contains(@class, "OrderFeed")]/li[1]')
    WINDOW_ORDER = (By.XPATH, './/div[contains(@class, "orderBox")]')
    ORDER_IN_PROGRESS = (By.XPATH, './/ul[contains (@class, "orderListReady")]')
    ORDER_FEED = (By.XPATH, ".//ul[contains(@class,'OrderFeed_list')]//p[contains(text(), '#')]")
    SUCCESSFULLY_ALL_TIME = (By.XPATH, ".//div[2]/p[2][contains (@class, 'OrderFeed')]")
    SUCCESSFULLY_TODAY_TIME = (By.XPATH, ".//div[3]/p[2][contains (@class, 'OrderFeed')]")

