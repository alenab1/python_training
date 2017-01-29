from model.contact import Contact
from random import randrange


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="None"))
    old_contacts_list = app.contact.get_contacts_list()
    index = randrange(len(old_contacts_list))
    print("index="+ str(index))
    contact = Contact(first_name="xxx", middle_name="yyy", last_name="zzz", address="addr88", home_tel="hoho", mobile_tel="+7",
                      work_tel="+1", phone2="98", email="asd@mail.ru", email2="qwe@mail.ru", email3="tre@gg.com")
    contact.id = old_contacts_list[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts_list) == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    contact.all_phones_from_home_page = app.contact.merge_phones(contact)
    contact.all_emails = app.contact.merge_emails(contact)
    old_contacts_list[index] = contact
    assert sorted(old_contacts_list, key=app.id_or_max) == sorted(new_contacts_list, key=app.id_or_max)



