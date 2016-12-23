
from model.contact import Contact


def test_add_contact(app):
        app.session.login(username="admin", password="secret")

        app.contact.create(
                        Contact(first_name="asd", middle_name="sdfgh", last_name="hjk", nickname="hoho", title="title",
                                company="comp", address="add", home_tel="+12", mobile_tel="+12", work_tel="+12",
                                fax="+12",
                                email="vhj@llk", email2="vgh@hvj", email3="vjk@vgh", homepage="page", birth_day="3",
                                birth_month="January", birth_year="2001", anniversary_day="3", anniversary_month="May",
                                anniversary_year="1999", address2="add",
                                phone2="phone2", notes="jl"))
        app.session.logout()


