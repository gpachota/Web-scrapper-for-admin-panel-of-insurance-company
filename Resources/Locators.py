from selenium.webdriver.common.by import By


class Locators():

    # --- Login Page Locators ---
    LOGIN_BUTTON = (By.XPATH, "//button[@onclick=\"f_login()\"]")
    USER_TEXT = (By.ID, "edtLogin")
    PASSWORD_TEXT = (By.ID, "edtPass")
    AFTER_LOGIN_TEXT = (By.XPATH, '//*[@id="contacts_list"]/h2')

    # --- Search Page Locators ---
    SEARCH_TEXTBOX = (By.XPATH, "//input[@id='edtMainSzkSearch']")
    SEARCH_SUBMIT_BUTTON = (By.XPATH, "//img[@onclick=\"sys.doSzkodaSzukaj();\"]")

    # --- Ticket Page Locators ---
    TICKET_NUMBER_DIV = (By.XPATH, "/html/body/div[1]/div[4]/div[1]/b")
    TICKET_DESCRIPTION_1 = (By.XPATH, "//div[@id=\"wrapper\"]/div[@id=\"szktop\"]/div[@class=\"naglowek\"]/div[2]/table/tbody/tr[3]/td[2]")
    TICKET_DESCRIPTION_2 = (By.XPATH, "//div[@id=\"wrapper\"]/div[@id=\"szktop\"]/div[@class=\"naglowek\"]/div[2]/table/tbody/tr[4]/td[2]")

    CUSTOMER_NAME_ID = (By.ID, "zglaszajacy")
    CUSTOMER_ADDRESS = (By.XPATH, "//div[@id=\"wrapper\"]/div[@id=\"szktop\"]/div[@class=\"naglowek\"]/div[2]/table/tbody/tr[2]/td[2]")

    INSURANCE_TYPE = (By.XPATH, "//div[@id=\"operationpanel\"]/div[@id=\"danepolisy\"]/div[@class=\"polcontent\"]/table/tbody/tr[1]/td[1]")
    INSURANCE_SUM = (By.XPATH, "//div[@id=\"operationpanel\"]/div[@id=\"danepolisy\"]/div[@class=\"polcontent\"]/table/tbody/tr[20]/td[2]")

    DEVICE_INFO_2 = (By.ID, "tdAsorAsortyment")
    DEVICE_INFO_1 = (By.ID, "tdAsorPrzedmiot")

    SHIPMENT_PAGE_LINK_LOCATOR = (By.XPATH, "//li[@onclick=\"sm.doWczytajKurier();\"]")
    SHIPMENT_PAGE_WAIT_ELEMENT = (By.CLASS_NAME, "kontaktmenu")
    SHIPMENT_FIRST_ELEMENT = "//table[@id=\"tabkon\"]/tbody/tr[1]/td[1]"

    POPUP_ERROR = "/html/body/div[4]"
    POPUP_OK_BUTTON = (By.XPATH, "//*[@id=\"popup_ok\"]")