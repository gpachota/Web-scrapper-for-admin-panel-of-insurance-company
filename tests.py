from main import *
from Resources.Locators import Locators
from Resources.CredentialData import UserData


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
        assert login() == 'Wiadomości'

    def test_quit(self):
        driver.quit()
