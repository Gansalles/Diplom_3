from selenium.webdriver.common.by import By


class EntrancePageLocators:
    TITLE_ENTRANCE = (By.XPATH, ".//h2[text() = 'Вход']")  # Название "Вход"
    BUTTON_ENTER = (By.XPATH, ".//button[text() = 'Войти']")  # Кнопка "Войти"
    PLACEHOLDER_EMAIL = (By.NAME, "name")  # поле логина
    PLACEHOLDER_PASSWORD = (By.NAME, "Пароль")  # поле пароля
    BUTTON_PASSWORD_RECOVERY = (By.XPATH, ".//a[text()='Восстановить пароль']")  # Кнопка
    # "Восстановления пароля"
