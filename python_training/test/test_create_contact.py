import re


def test_add_contact(app, json_contacts):
        contact = json_contacts
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




