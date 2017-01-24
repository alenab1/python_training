from model.contact import Contact
import re


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
        self.contact_cache = None

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
                                    "//select[@name='bday']//option[@value='%s']" % contact.birth_day).is_selected():
                wd.find_element_by_xpath("//select[@name='bday']//option[@value='%s']" % contact.birth_day).click()
        if contact.birth_month is not None:
            if not wd.find_element_by_xpath(
                                "//select[@name='bmonth']//option[@value='%s']" % contact.birth_month).is_selected():
                wd.find_element_by_xpath("//select[@name='bmonth']//option[@value='%s']" % contact.birth_month).click()

        self.app.change_field_value("byear", contact.birth_year)
        if contact.anniversary_day is not None:
            if not wd.find_element_by_xpath(
                                "//select[@name='aday']//option[@value='%s']" % contact.anniversary_day).is_selected():
                wd.find_element_by_xpath("//select[@name='aday']//option[@value='%s']" % contact.anniversary_day).click()
        if contact.anniversary_month is not None:
            if not wd.find_element_by_xpath(
                                "//select[@name='amonth']//option[@value='%s']" % contact.anniversary_month).is_selected():
                wd.find_element_by_xpath(
                "//select[@name='amonth']//option[@value='%s']" % contact.anniversary_month).click()

        self.app.change_field_value("ayear", contact.anniversary_year)
        self.app.change_field_value("address2", contact.address2)
        self.app.change_field_value("phone2", contact.phone2)
        self.app.change_field_value("notes", contact.notes)

    def delete_first_contact(self):
        self.delete_contact_by_index(1)

    def edit_first(self, contact):
        self.edit_contact_by_index(self, 1, contact)

    def count(self):
        wd = self.app.wd
        self.app.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.go_to_home_page()
            contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                f_name = cells[2].text
                l_name = cells[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                address = cells[3].text
                all_emails = cells[4].text
                contact_cache.append(Contact(first_name=f_name, last_name=l_name, id=id, address=address,
                                             all_phones_from_home_page=all_phones, all_emails=all_emails))
        return list(contact_cache)

    def open_contact_for_edit_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_xpath("//tr[@name='entry'][%s]//img[@title='Edit']/.." % str(index+1)).click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.click_checkbox_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deletion alert
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.go_to_home_page()
        # init contact editing
        self.open_contact_for_edit_by_index(index)
        # fill contact form with new values
        self.fill_contact_form(contact)
        # submit editing
        wd.find_element_by_xpath("//input[@type='submit' and @value='Update']").click()
        self.contact_cache = None

    def open_contact_details_by_index(self, index):
        wd = self.app.wd
        self.app.go_to_home_page()
        #open contact details
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.app.go_to_home_page()
        self.open_contact_for_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_tel = wd.find_element_by_name("home").get_attribute("value")
        mobile_tel = wd.find_element_by_name("mobile").get_attribute("value")
        work_tel = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id, first_name = first_name, last_name=last_name, home_tel=home_tel, mobile_tel=mobile_tel, work_tel=work_tel,
                       phone2=phone2, address=address, email=email, email2=email2, email3=email3)

    def get_contacts_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_details_by_index(index)
        contact_content = wd.find_element_by_id("content").text
        home_tel = ""
        mobile_tel = ""
        work_tel = ""
        phone2 = ""
        if "H:" in contact_content:
            home_tel = re.search("H: (.*)", contact_content).group(1)
        if "M:" in contact_content:
            mobile_tel = re.search("M: (.*)", contact_content).group(1)
        if "W:" in contact_content:
            work_tel = re.search("W: (.*)", contact_content).group(1)
        if "P:" in contact_content:
            phone2 = re.search("P: (.*)", contact_content).group(1)
        return Contact(home_tel=home_tel, mobile_tel=mobile_tel,
                       work_tel=work_tel,
                       phone2=phone2)

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def merge_phones(self, contact):
        return "\n".join(filter(lambda x: x != "",
                        map(lambda x: self.clear(x),
                                filter(lambda x: x is not None,
                                        [contact.home_tel, contact.mobile_tel,
                                            contact.work_tel, contact.phone2]))))

    def merge_emails(self, contact):
        contact.email = contact.email.strip()
        contact.email2 = contact.email2.strip()
        contact.email3 = contact.email3.strip()
        whole_email = "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                    [contact.email, contact.email2,
                                        contact.email3])))
        whole_email = re.sub(" +", " ", whole_email)
        return whole_email
