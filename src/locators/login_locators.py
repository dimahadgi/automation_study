from selenium.webdriver.common.by import By

EMAIL = (By.NAME, 'username')
PASSWORD = (By.NAME, 'password')
LOGIN = (By.CSS_SELECTOR, 'button[type="submit"]')
GRID = (By.XPATH, '//div[@role="grid"]')
LOGO = (By.XPATH, '//img[@alt="SkillsPass"]')