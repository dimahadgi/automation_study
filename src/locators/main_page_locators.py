from selenium.webdriver.common.by import By


# main menu
CERTIFICATES_TAB = (By.CSS_SELECTOR, 'a[href="/employer-client/certificates"]')
HELP = (By.XPATH, '//button/span[text()="Help"]')
LANGUAGE_SWITCH = (By.XPATH, '//div/div[text()="EN"]')
SIGN_OUT = (By.XPATH, '//button/span[text()="Sign out"]')

# controls
ADD_NEW_WORKER = (By.XPATH, '//button/span[text()="Add new worker"]')
IMPORT_WORKER = (By.XPATH, 'svg path[d*="M21 5c-1"]')
SAVE_REPORT = (By.XPATH, 'svg path[d*="M9 11.3l3"]')
SAVED_REPORTS = (By.XPATH, 'g path[d*="M11,12"]')
PROJECT_TEAMS = (By.XPATH, 'g path[d*="M13.5333333"]')
SHARED = (By.XPATH, 'svg path[d*="M6.99"]')

# fields
SEARCH = (By.CSS_SELECTOR, 'form input[type="text"]')

# filters
WORKER_STATUS_FILTER = (By.XPATH, '//button/span[text()="Workers status"]')
CERTIFICATE_STATUS_FILTER = (By.XPATH, '//button/span[text()="Certificate status"]')
COURSE_FILTER = (By.XPATH, '//button/span[text()="Course"]')
TRADES_FILTER = (By.XPATH, '//button/span[text()="Trade"]')
SYNC_BUTTON = (By.XPATH, '//button/span[text()="Sync"]')


# add new worker test
EMAIL_ADDRESS_FIELD = (By.CSS_SELECTOR, 'form div [type="email"]')
SEARCH_EMAILS_BUTTON = (By.XPATH, '//button/span[text()="Search"]')
FIRST_NAME_FIELD = (By.CSS_SELECTOR, 'form #firstname')
LAST_NAME_FIELD = (By.CSS_SELECTOR, 'form #lastname')
CREATE_WORKER_BUTTON = (By.XPATH, '//button/span[text()="Create"]')
CONFIRMATION_MESSAGE = (By.XPATH, '//span[contains(text(),"created")]')

