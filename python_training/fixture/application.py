from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from sys import maxsize


class Application:
    def __init__(self):
        self.wd = WebDriver()
        #self.wd.implicitly_wait(8)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    def change_field_value(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def click_first_entry_in_list(self):
        wd = self.wd
        wd.find_element_by_name("selected[]").click()

    def go_to_home_page(self):
        wd = self.wd
        address = wd.current_url
        if not (address.endswith("addressbook/") or address.endswith("/index.php")):
            wd.find_element_by_link_text("home").click()

    def id_or_max(self, gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize


