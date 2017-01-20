import re
from random import randrange


def test_phones_at_home_page(app):
    contacts_from_home_page = app.contact.get_contacts_list()
    index_to_check = randrange(len(contacts_from_home_page))
    contact_to_check_from_home_page = contacts_from_home_page[index_to_check]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index_to_check)
    assert contact_to_check_from_home_page.all_phones_from_home_page == merge_phones(contact_from_edit_page)
    #assert for email addresses
    assert contact_to_check_from_home_page.all_emails == merge_emails(contact_from_edit_page)
    #first name
    assert contact_to_check_from_home_page.first_name == contact_from_edit_page.first_name
    #last name
    assert contact_to_check_from_home_page.last_name == contact_from_edit_page.last_name
    #address
    assert contact_to_check_from_home_page.address == contact_from_edit_page.address


def test_phones_at_contact_view_page(app):
    contact_from_view_page = app.contact.get_contacts_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_tel == contact_from_edit_page.home_tel
    assert contact_from_view_page.mobile_tel == contact_from_edit_page.mobile_tel
    assert contact_from_view_page.work_tel == contact_from_edit_page.work_tel
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                        [contact.home_tel, contact.mobile_tel,
                                            contact.work_tel, contact.phone2]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                    [contact.email, contact.email2,
                                        contact.email3])))
