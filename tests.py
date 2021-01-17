from main import *
from Resources.Locators import Locators
from Resources.CredentialData import UserData, TestData


class TestMain:
    def test_send_keys(self):
        send_keys(Locators.USER_TEXT, UserData.username)
        send_keys(Locators.PASSWORD_TEXT, UserData.password)

        assert driver.find_element_by_id('edtLogin').get_attribute('value') == UserData.username
        assert driver.find_element_by_id('edtPass').get_attribute('value') == UserData.password

    def test_clear_text(self):
        clear_keys(Locators.USER_TEXT)
        clear_keys(Locators.PASSWORD_TEXT)

        assert driver.find_element_by_id('edtLogin').get_attribute('value') == ''
        assert driver.find_element_by_id('edtPass').get_attribute('value') == ''

    def test_login(self):
        assert login() == TestData.HELLO_TEXT

    def test_tickets_import(self):
        global imported_tickets
        imported_tickets = SheetsImport().import_data()
        assert tickets_import() == imported_tickets

    def test_make_dataframe(self):
        global df
        column_list = ['ticket_number', 'customer_name', 'customer_adress', 'insurance_type', 'insurance_sum',
                       'device_info1', 'device_info2', 'device_model', 'ordered_shipment', 'shipment_date',
                       'ticket_description', 'ticket_circumstances', 'colour', 'complaint']

        df = pd.DataFrame(np.nan, index=np.arange(len(imported_tickets)), columns=column_list)
        df['ticket_number'][0:len(imported_tickets)] = imported_tickets
        assert make_dataframe().equals(df)

    def test_open_new_tickets(self):
        pass

    def test_quit(self):
        driver.quit()
