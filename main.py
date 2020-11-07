# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from device import set_model_name, set_device_colour

from Resources.Locators import Locators

from Resources.CredentialData import UserData, MainData

from SheetsInOut import SheetsImport, SheetsExport





def click(locator):
    """Find element with specific path and click in it"""
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator)).click()
    return None


def send_keys(locator, key):
    """Find inout element and send keys in it"""
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(key)
    return None


def get_text(locator):
    """Find element and get text from it"""
    return WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator)).text

def clear_keys(locator):
    """clear input element"""
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator)).clear()
    return None

def login():
    """Login to website"""
    send_keys(Locators.USER_TEXT, UserData.username)
    send_keys(Locators.PASSWORD_TEXT, UserData.password)
    click(Locators.LOGIN_BUTTON)

    print("Logged in")
    return None


def tickets_import():
    tickets_import = SheetsImport().importData()
    tickets_list = []
    x = 0

    for i in tickets_import:
        if open_ticket(i) != True:
            click(Locators.POPUP_OK_BUTTON)
        else:
            tickets = get_ticket_info(i, len(tickets_import), tickets_import)
            tickets_list.append([])
            tickets_list[x].append(tickets)
            x += 1
    return tickets_list


def open_ticket(ticketnumber):
    """Find search input element, put text in it and hit search button. Check if there is no error popup and if not - go to the fresh open cart in chrome."""
    clear_keys(Locators.SEARCH_TEXTBOX)
    send_keys(Locators.SEARCH_TEXTBOX, ticketnumber)
    click(Locators.SEARCH_SUBMIT_BUTTON)

    if check_exists_by_xpath("//*[@id=\"popup_ok\"]"):
        return False
    else:
        # switch to new window
        driver.switch_to.window(driver.window_handles[-1])
        print(str(ticketnumber) + " opened")
        return True

def get_ticket_number():
    """Get ticket number"""
    ticket_number = get_text(Locators.TICKET_NUMBER_DIV)

    return ticket_number


def get_ticket_description():
    """Get ticket description"""
    description = get_text(Locators.TICKET_DESCRIPTION_1)
    circumstances = get_text(Locators.TICKET_DESCRIPTION_2)

    return description, circumstances

def get_customer_info():
    """Get customer info"""
    name = get_text(Locators.CUSTOMER_NAME_ID)
    address = get_text(Locators.CUSTOMER_ADDRESS)

    return name, address

def get_insurance_type():
    """Get insurance type info"""
    insurance_type_readed = get_text(Locators.INSURANCE_TYPE)
    insurance_type = check_insurance_type(insurance_type_readed)

    return insurance_type

def check_insurance_type(insurance_type):
    """Check if insurance type is acutally in base dictionary"""
    if "WARIANT PEŁNY" in insurance_type:
        insurance_type = "WARIANT PEŁNY"

    elif insurance_type[:14].upper() == "OCHRONA EKRANU":
        insurance_type = "OCHRONA EKRANU"

    elif insurance_type == "1) konsumpcja SU, 2) udział własny":
        insurance_type = "UDZIAŁ WŁASNY 20%"

    return insurance_type

def get_insurance_sum():
    """Get insurance sum"""
    insurance_sum = driver.find_element_by_xpath(
        "//div[@id=\"operationpanel\"]/div[@id=\"danepolisy\"]/div[@class=\"polcontent\"]/table/tbody/tr[20]/td[2]").text

    return insurance_sum

def get_device_info():
    """Get device info"""
    info_1 = get_text(Locators.DEVICE_INFO_1)
    info_2 = get_text(Locators.DEVICE_INFO_2)

    return info_1, info_2

def get_ticket_info(i, tickets_import_length, tickets_import):

    # wait until site is ready
    ticket_number = get_ticket_number()
    ticket_description, ticket_circumstances = get_ticket_description()

    # customer data
    customer_name, customer_adress = get_customer_info()

    # insurance data
    insurance_type = get_insurance_type()
    insurance_sum = get_insurance_sum()

    # device info
    device_info1, device_info2 = get_device_info()

    # shipment info
    shipment_date = get_shipment_date()

    print(str(tickets_import.index(i)+1) + "/" +
          str(tickets_import_length) + " Done")

    if device_info2 != "":
        model = set_model_name(device_info2)
        colour = set_device_colour(device_info2)
        return (ticket_number, customer_name, customer_adress, insurance_type, insurance_sum, device_info1, model, shipment_date, ticket_description, ticket_circumstances, colour)
    elif device_info2 == "":
        model = set_model_name(device_info1)
        colour = set_device_colour(device_info1)
        return (ticket_number, customer_name, customer_adress, insurance_type, insurance_sum, device_info1, model, shipment_date, ticket_description, ticket_circumstances, colour)
    else:
        colour = ""
        return (ticket_number, customer_name, customer_adress, insurance_type, insurance_sum, device_info1, device_info2, shipment_date, ticket_description, ticket_circumstances, colour)


def get_shipment_date():

    # go into "kurier"

    click(Locators.SHIPMENT_PAGE_LINK_LOCATOR)

    # wait until site is ready
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(Locators.SHIPMENT_PAGE_WAIT_ELEMENT))

    # check if there is any shipment info
    if check_exists_by_xpath(Locators.SHIPMENT_FIRST_ELEMENT) == True:
        # if exists - check first info
        print(True)
        i = 1
        shipment_exist = driver.find_element_by_xpath(
            "//table[@id=\"tabkon\"]/tbody/tr[" + str(i) + "]/td[1]").text
        print(shipment_exist)
        # searching for shipping in
        while shipment_exist != "Odebranie sprzętu do naprawy":
            if shipment_exist == "Reklamacja Odebranie sprzętu do naprawy":
                break
            elif shipment_exist == "Zwrot sprzętu z naprawy do klienta":
                break
            else:
                i += 1
                shipment_exist = driver.find_element_by_xpath(
                    "//table[@id=\"tabkon\"]/tbody/tr[" + str(i) + "]/td[1]").text
                print(+1)
        # take date of shippment
        if shipment_exist == "Zwrot sprzętu z naprawy do klienta":
            shipment_date = "ZWROT"
        else:
            shipment_date = driver.find_element_by_xpath(
                "//table[@id=\"tabkon\"]/tbody/tr[" + str(i) + "]/td[3]").text
        print(shipment_date)
    else:
        shipment_date = ""

    return shipment_date
    # check_exists_by_xpath("//table[@id=\"tabkon\"]")


def check_exists_by_xpath(xpath):
    """Sprawdzenie czy ścieżka XPATH istnieje"""
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


try:
    driver = webdriver.Chrome(MainData.CHROME_EXECUTABLE_PATH)
    driver.get(MainData.BASE_URL)
    login()
    SheetsImport().cleanSheet(
        SheetsExport().exportAllData(
            tickets_import()
            )
        )
finally:
    driver.quit()
    print("Done")