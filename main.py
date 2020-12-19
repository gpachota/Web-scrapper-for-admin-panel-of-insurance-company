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

import numpy as np
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')



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

def update_df_cell(row, column, value):
    df.loc[df['ticket_number'] == int(row), column] = value


def tickets_import():
    tickets_import = SheetsImport().importData()

    feature_list = ['ticket_number', 'customer_name', 'customer_adress', 'insurance_type', 'insurance_sum',
                'device_info1', 'device_info2', 'device_model', 'shipment_date', 'ticket_description', 'ticket_circumstances', 'colour']

    global df
    df = pd.DataFrame(np.nan, index=np.arange(len(tickets_import)), columns=feature_list)
    df['ticket_number'][0:len(tickets_import)] = tickets_import

    for i in tickets_import:
        if open_ticket(i) != True:
            click(Locators.POPUP_OK_BUTTON)
        else:
            tickets = get_ticket_info(i, len(tickets_import), tickets_import)
    return df


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
    global ticket_number
    ticket_number = get_text(Locators.TICKET_NUMBER_DIV)

    return ticket_number


def get_ticket_description():
    """Get ticket description"""

    update_df_cell(ticket_number, 'ticket_description', get_text(Locators.TICKET_DESCRIPTION_1))
    update_df_cell(ticket_number, 'ticket_circumstances', get_text(Locators.TICKET_DESCRIPTION_2))

    return None

def get_customer_info():
    """Get customer info"""

    update_df_cell(ticket_number, 'customer_name', get_text(Locators.CUSTOMER_NAME_ID))
    update_df_cell(ticket_number, 'customer_adress', get_text(Locators.CUSTOMER_ADDRESS))

    return None

def get_insurance_type():
    """Get insurance type info"""
    global insurance_type

    insurance_type_readed = get_text(Locators.INSURANCE_TYPE)
    insurance_type = check_insurance_type(insurance_type_readed)

    update_df_cell(ticket_number, 'insurance_type', insurance_type)

    return None

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
    if insurance_type == "partner":
        insurance_sum = driver.find_element_by_xpath(
            "/html/body/div[1]/div[6]/div[1]/div/table/tbody/tr[18]/td[2]").text
    else:
        insurance_sum = driver.find_element_by_xpath(
            "//div[@id=\"operationpanel\"]/div[@id=\"danepolisy\"]/div[@class=\"polcontent\"]/table/tbody/tr[20]/td[2]").text

    update_df_cell(ticket_number, 'insurance_sum', insurance_sum)

    return None

def get_device_info():
    """Get device info"""
    global device_info1
    global device_info2
    device_info1 = get_text(Locators.DEVICE_INFO_1)
    device_info2 = get_text(Locators.DEVICE_INFO_2)

    update_df_cell(ticket_number, 'device_info1', get_text(Locators.DEVICE_INFO_1))
    update_df_cell(ticket_number, 'device_info2', get_text(Locators.DEVICE_INFO_2))

    return None

def get_ticket_info(i, tickets_import_length, tickets_import):

    # wait until site is ready
    get_ticket_number()
    get_ticket_description()

    # customer data
    get_customer_info()

    # insurance data
    get_insurance_type()
    get_insurance_sum()

    # device info
    get_device_info()

    # shipment info
    update_df_cell(ticket_number, 'shipment_date', get_shipment_date())

    print(str(tickets_import.index(i)+1) + "/" +
          str(tickets_import_length) + " Done")

    if device_info2 != "":

        update_df_cell(ticket_number, 'device_model', set_model_name(device_info2))
        update_df_cell(ticket_number, 'colour', set_device_colour(device_info2))

    elif device_info2 == "":

        update_df_cell(ticket_number, 'device_model', set_model_name(device_info1))
        update_df_cell(ticket_number, 'colour', set_device_colour(device_info1))

    return None

def get_shipment_date():

    # go into "kurier"

    click(Locators.SHIPMENT_PAGE_LINK_LOCATOR)

    # wait until site is ready
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(Locators.SHIPMENT_PAGE_WAIT_ELEMENT))

    # check if there is any shipment info
    if check_exists_by_xpath(Locators.SHIPMENT_FIRST_ELEMENT) == True:
        # if exists - check first info
        i = 1
        shipment_exist = driver.find_element_by_xpath(
            "//table[@id=\"tabkon\"]/tbody/tr[" + str(i) + "]/td[1]").text
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
    """Check if xpath exist"""
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


try:
    driver = webdriver.Chrome(MainData.CHROME_EXECUTABLE_PATH, options=chrome_options)
    driver.get(MainData.BASE_URL)
    login()
    SheetsExport().exportDataFrame(
            tickets_import()
        )
    SheetsImport().cleanSheet()
finally:
    driver.quit()
    print("Done")