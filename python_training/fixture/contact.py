
class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.go_to_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        #submit creation
        wd.find_element_by_xpath("//input[@type='submit' and @value='Enter']").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.app.change_field_value("firstname", contact.first_name)
        self.app.change_field_value("middlename", contact.middle_name)
        self.app.change_field_value("lastname", contact.last_name)
        self.app.change_field_value("nickname", contact.nickname)
        self.app.change_field_value("title", contact.title)
        self.app.change_field_value("company", contact.company)
        self.app.change_field_value("address", contact.address)
        self.app.change_field_value("home", contact.home_tel)
        self.app.change_field_value("mobile", contact.mobile_tel)
        self.app.change_field_value("work", contact.work_tel)
        self.app.change_field_value("fax", contact.fax)
        self.app.change_field_value("email", contact.email)
        self.app.change_field_value("email2", contact.email2)
        self.app.change_field_value("email3", contact.email3)
        self.app.change_field_value("homepage", contact.homepage)
        if contact.birth_day is not None:
            if not wd.find_element_by_xpath(
                                    "//select[@name='bday']//option[@value='" + contact.birth_day + "']").is_selected():
                wd.find_element_by_xpath("//select[@name='bday']//option[@value='" + contact.birth_day + "']").click()
        if contact.birth_month is not None:
            if not wd.find_element_by_xpath(
                                "//select[@name='bmonth']//option[@value='" + contact.birth_month + "']").is_selected():
                wd.find_element_by_xpath("//select[@name='bmonth']//option[@value='" + contact.birth_month + "']").click()

        self.app.change_field_value("byear", contact.birth_year)
        if contact.anniversary_day is not None:
            if not wd.find_element_by_xpath(
                                "//select[@name='aday']//option[@value='" + contact.anniversary_day + "']").is_selected():
                wd.find_element_by_xpath("//select[@name='aday']//option[@value='" + contact.anniversary_day + "']").click()
        if contact.anniversary_month is not None:
            if not wd.find_element_by_xpath(
                                "//select[@name='amonth']//option[@value='" + contact.anniversary_month + "']").is_selected():
                wd.find_element_by_xpath(
                "//select[@name='amonth']//option[@value='" + contact.anniversary_month + "']").click()

        self.app.change_field_value("ayear", contact.anniversary_year)
        self.app.change_field_value("address2", contact.address2)
        self.app.change_field_value("phone2", contact.phone2)
        self.app.change_field_value("notes", contact.notes)

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.go_to_home_page()
        self.app.click_first_entry_in_list()
        # init contact deletion
        wd.find_element_by_xpath("//input[@type='button' and @value='Delete']").click()
        #submit deletion alert
        wd.switch_to_alert().accept()

    def edit_first(self, contact):
        wd = self.app.wd
        self.app.go_to_home_page()
        # init contact editing
        wd.find_element_by_xpath("//tr[@name='entry'][1]//img[@title='Edit']/..").click()
        # fill contact form with new values
        self.fill_contact_form(contact)
        #submit editing
        wd.find_element_by_xpath("//input[@type='submit' and @value='Update']").click()

    def count(self):
        wd = self.app.wd
        self.app.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))
