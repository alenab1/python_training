
class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.go_to_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        #submit creation
        wd.find_element_by_xpath("//input[@type='submit' and @value='Enter']").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_tel)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_tel)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_tel)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        if not wd.find_element_by_xpath(
                                "//select[@name='bday']//option[@value='" + contact.birth_day + "']").is_selected():
            wd.find_element_by_xpath("//select[@name='bday']//option[@value='" + contact.birth_day + "']").click()
        if not wd.find_element_by_xpath(
                                "//select[@name='bmonth']//option[@value='" + contact.birth_month + "']").is_selected():
            wd.find_element_by_xpath("//select[@name='bmonth']//option[@value='" + contact.birth_month + "']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birth_year)
        if not wd.find_element_by_xpath(
                                "//select[@name='aday']//option[@value='" + contact.anniversary_day + "']").is_selected():
            wd.find_element_by_xpath("//select[@name='aday']//option[@value='" + contact.anniversary_day + "']").click()
        if not wd.find_element_by_xpath(
                                "//select[@name='amonth']//option[@value='" + contact.anniversary_month + "']").is_selected():
            wd.find_element_by_xpath(
                "//select[@name='amonth']//option[@value='" + contact.anniversary_month + "']").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def delete_first_contact(self):
        wd = self.app.wd
        self.go_to_home_page()
        self.click_first_entry_in_list()
        # init contact deletion
        wd.find_element_by_xpath("//input[@type='button' and @value='Delete']").click()
        #submit deletion alert
        wd.switch_to_alert().accept()

    def click_first_entry_in_list(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def go_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def edit_first(self, contact):
        wd = self.app.wd
        self.go_to_home_page()
        # init contact editing
        wd.find_element_by_xpath("//tr[@name='entry'][1]//img[@title='Edit']/..").click()
        # fill contact form with new values
        self.fill_contact_form(contact)
        #submit editing
        wd.find_element_by_xpath("//input[@type='submit' and @value='Update']").click()


