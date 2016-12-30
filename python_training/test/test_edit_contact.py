from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="None"))
    app.contact.edit_first(Contact(first_name="xxx", middle_name="yyy", last_name="zzz"))

