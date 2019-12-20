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

# edit personal data via profile
WORKER_IN_THE_GRID = (By.CSS_SELECTOR, '.ag-pinned-left-cols-container .ag-react-container div p')
EDIT_PROFILE_CONTROL = (By.CSS_SELECTOR, 'svg path[d*="M3 17.25V21h3"]')
SEARCH = (By.CSS_SELECTOR, 'main div form input[type="text"]')
SUBMIT_BUTTON = (By.CSS_SELECTOR, 'form button[type="submit"]')
FILTERS_SECTION = (By.CSS_SELECTOR, 'div #filters')
EMAIL_FIELD_IN_EDIT_MODAL = (By.CSS_SELECTOR, 'div #email')
DONE_BUTTON_IN_EDIT_MODAL = (By.XPATH, '//button/span[text()="Done"]')

# upload files
ADD_NEW_RECORD = (By.XPATH, '//button/span[text()="Add training records"]')
INPUT_FOR_UPLOAD_BUTTON = (By.CSS_SELECTOR, '''div[role="dialog"] input[type="file"]''')
SELECT_DROP_DOWN = (By.XPATH, '//div[text()="select..."]')
FIRST_ITEM_IN_DROP_DOWN = (By.XPATH, '//ul[@role="listbox"]//li[text()="1"]')
CERTIFICATE_TITLE = (By.CSS_SELECTOR, '#certificateTitle1')
TRAINING_PROVIDER_NAME = (By.CSS_SELECTOR, '#trainingProviderName1')
ISSUED_DATE = (By.CSS_SELECTOR, '#certificateIssueDate1')
EXPIRY_DATE = (By.CSS_SELECTOR, '#certificateExpiryDate1')
FINISH_BUTTON = (By.XPATH, '//button/span[text()="Finish"]')
ADDITIONAL_DETAILS_FIELD = (By.CSS_SELECTOR, '#additionalCertificateDetails1')
WAIT_FOR_CONF_MESSAGE = (By.XPATH, '//p[contains(text(),"added for")]')

# archive worker
CHECKBOXES_NEXT_TO_WORKERS_IN_GRID = (By.CSS_SELECTOR, '.ag-pinned-left-cols-container div span')
ARCHIVE_BUTTON = (By.XPATH, '//button/span[text()="Archive"]')
ARCHIVE_BUTTON_IN_DIALOG = (By.XPATH, '''//div[@role='dialog']//button/span[text()="Archive"]''')
CONFIRMATION_MESSAGE_FOR_ARCH_WORKER = (By.XPATH, '''//div[@role='dialog']//p[contains(text(), "archived")]''')



