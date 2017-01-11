from model.contact import Contact
from random import randrange


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="None"))
    old_contacts_list = app.contact.get_contacts_list()
    index = randrange(len(old_contacts_list))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts_list) - 1 == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    old_contacts_list[index:index+1] = []
    assert old_contacts_list == new_contacts_list
