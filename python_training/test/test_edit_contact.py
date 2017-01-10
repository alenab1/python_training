from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="None"))
    old_contacts_list = app.contact.get_contacts_list()
    contact = Contact(first_name="xxx", middle_name="yyy", last_name="zzz")
    contact.id = old_contacts_list[0].id
    app.contact.edit_first(contact)
    new_contacts_list = app.contact.get_contacts_list()
    assert len(old_contacts_list) == len(new_contacts_list)
    old_contacts_list[0] = contact
    assert sorted(old_contacts_list, key=app.id_or_max) == sorted(new_contacts_list, key=app.id_or_max)



