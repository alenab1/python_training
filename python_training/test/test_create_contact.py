
from model.contact import Contact
import pytest
import random
import string
import datetime
import re


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*25
    # symbols = string.ascii_letters + string.digits + " " * 25
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_month():
    return random.choice(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                   'October', 'November', 'December'])

testdata = [Contact(first_name="", last_name="", address="", home_tel="", mobile_tel="", work_tel="",
                                email="", email2="", email3="", phone2="",

                    )] + [Contact(first_name=random_string("first_name ", 10),

                                                                 last_name=random_string("last_name ", 10),
                                                                 address=random_string("address ", 10),
                                home_tel=random_string("home_tel ", 10), mobile_tel=random_string("mobile_tel ", 10),
                                work_tel=random_string("work_tel ", 10),
                                email=random_string("email", 10), email2=random_string("email2", 10),
                                email3=random_string("email3", 10),
                                phone2=random_string("phone2 ", 10)) for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
        old_contacts_list = app.contact.get_contacts_list()
        app.contact.create(contact)
        assert len(old_contacts_list) + 1 == app.contact.count()
        new_contacts_list = app.contact.get_contacts_list()
        contact.address = contact.address.strip()
        contact.first_name = contact.first_name.strip()
        contact.last_name = contact.last_name.strip()
        contact.address = re.sub(" +", " ", contact.address)
        contact.first_name = re.sub(" +", " ", contact.first_name)
        contact.last_name = re.sub(" +", " ", contact.last_name)
        contact.all_phones_from_home_page = app.contact.merge_phones(contact)
        contact.all_emails = app.contact.merge_emails(contact)
        old_contacts_list.append(contact)

        print(sorted(old_contacts_list, key=app.id_or_max))
        print(sorted(new_contacts_list, key=app.id_or_max))
        assert sorted(old_contacts_list, key=app.id_or_max) == sorted(new_contacts_list, key=app.id_or_max)




