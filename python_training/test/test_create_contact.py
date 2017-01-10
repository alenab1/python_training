
from model.contact import Contact


def test_add_contact(app):
        old_contacts_list = app.contact.get_contacts_list()
        contact = Contact(first_name="asd", middle_name="sdfgh", last_name="hjk", nickname="hoho", title="title",
                                company="comp", address="add", home_tel="+12", mobile_tel="+12", work_tel="+12",
                                fax="+12",
                                email="vhj@llk", email2="vgh@hvj", email3="vjk@vgh", homepage="page", birth_day="3",
                                birth_month="January", birth_year="2001", anniversary_day="3", anniversary_month="May",
                                anniversary_year="1999", address2="add",
                                phone2="phone2", notes="jl")
        app.contact.create(
                        contact)
        new_contacts_list = app.contact.get_contacts_list()
        assert len(old_contacts_list) + 1 == len(new_contacts_list)
        old_contacts_list.append(contact)
        assert sorted(old_contacts_list, key=app.id_or_max) == sorted(new_contacts_list, key=app.id_or_max)




