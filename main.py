# -*- coding: utf-8 -*-

from driver_setup import start_chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from device import set_model_name, set_device_colour

from Resources.Locators import Locators
from Resources.CredentialData import UserData, MainData

from SheetsInOut import SheetsImport, SheetsExport

import numpy as np
import pandas as pd

global driver
driver = start_chrome(MainData.BASE_URL, MainData.CHROME_EXECUTABLE_PATH)


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
    return get_text(Locators.AFTER_LOGIN_TEXT)


def update_df_cell(row, column, value):
    df.loc[df['ticket_number'] == int(row), column] = value


def tickets_import():
    global imported_tickets
    imported_tickets = SheetsImport().importData()

    feature_list = ['ticket_number', 'customer_name', 'customer_adress', 'insurance_type', 'insurance_sum',
                    'device_info1', 'device_info2', 'device_model', 'ordered_shipment', 'shipment_date',
                    'ticket_description', 'ticket_circumstances', 'colour', 'complaint']

    global df
    df = pd.DataFrame(np.nan, index=np.arange(len(imported_tickets)), columns=feature_list)
    df['ticket_number'][0:len(imported_tickets)] = imported_tickets

    for i in imported_tickets:
        if not open_ticket(i):
            click(Locators.POPUP_OK_BUTTON)
            update_df_cell(i, 'ordered_shipment', 'DEL')
        else:
            get_ticket_info(i, len(imported_tickets), imported_tickets)

    existing = SheetsExport().importOldDataFrame()
    existing_length = len(existing['ticket_number'].tolist())

    for i in imported_tickets:
        if existing_length > 0:
            if i in existing['ticket_number'].tolist():
                if df.loc[df.ticket_number == i]['ordered_shipment'].values[0] == 'YES':
                    existing.loc[existing['ticket_number'] == i, 'shipment_date'] = df.loc[df.ticket_number == i]['shipment_date'].values[0]
                    existing.loc[existing['ticket_number'] == i, 'ordered_shipment'] = df.loc[df.ticket_number == i]['ordered_shipment'].values[0]
                    df.drop(df[df['ticket_number'] == i].index, inplace = True)

    df_final = existing.append(df)
    df_final.drop_duplicates(subset = 'ticket_number', keep = 'first', inplace=True)

    return df_final


def open_ticket(ticketnumber):
    """Find search input element, put text in it and hit search button.
    Check if there is no error popup and if not - go to the fresh open cart in chrome."""
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
    ticket_number_color = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/b")\
        .value_of_css_property('color')
    if ticket_number_color == "rgba(255, 0, 0, 1)":
        update_df_cell(ticket_number, 'complaint', 'Reklamacja')

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
    shipment_date = get_shipment_date()
    if shipment_date != "":
        update_df_cell(ticket_number, 'shipment_date', shipment_date)
        update_df_cell(ticket_number, 'ordered_shipment', 'YES')
    else:
        update_df_cell(ticket_number, 'ordered_shipment', 'NO')

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
    if check_exists_by_xpath(Locators.SHIPMENT_FIRST_ELEMENT):
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
            elif shipment_exist == 'Odebranie sprzętu zastępczego od klienta':
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


if __name__ == "__main__":
    login()
    SheetsExport().exportDataFrame(
        tickets_import()
    )
    SheetsImport().cleanSheet(imported_tickets)
    print("Done")
    driver.quit()