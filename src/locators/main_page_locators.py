from selenium.webdriver.common.by import By


# main menu
CERTIFICATES_TAB = (By.CSS_SELECTOR, 'a[href*="/employer-client/certificates"]')
HELP = (By.XPATH, '//button/span[text()="Help"]')
LANGUAGE_SWITCH = (By.XPATH, '//div/div[text()="EN"]')
SIGN_OUT = (By.XPATH, '//button/span[text()="Sign out"]')

# controls
ADD_NEW_WORKER = (By.XPATH, '//button/span[text()="Add new worker"]')
IMPORT_WORKER = (By.XPATH, '//button/span[text()="Import workers"]')
SAVE_REPORT = (By.XPATH, '//button/span[text()="Save report"]')
SAVED_REPORTS = (By.XPATH, '//button/span[text()="Saved reports"]')
PROJECT_TEAMS = (By.XPATH, '//button/span[text()="Project Teams"]')
SHARED = (By.XPATH, '//button/span[text()="Shared"]')

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
FIRST_NAME_FIELD = (By.CSS_SELECTOR, 'form div #firstname')
LAST_NAME_FIELD = (By.CSS_SELECTOR, 'form div #lastname')
CREATE_WORKER_BUTTON = (By.XPATH, '//button/span[text()="Create"]')

