
class Contact:
    def __init__(self, id=None, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None, address=None, home_tel=None,
                       mobile_tel=None, work_tel=None, fax=None, email=None, email2=None, email3=None, homepage=None, birth_day=None, birth_month=None, birth_year=None,
                       anniversary_day=None, anniversary_month=None, anniversary_year=None, address2=None, phone2=None, notes=None,
                 all_phones_from_home_page=None, all_emails=None):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_tel = home_tel
        self.mobile_tel = mobile_tel
        self.work_tel = work_tel
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails = all_emails

    def __repr__(self):
        return "%s;%s:%s:%s:%s:%s" % (self.id, self.first_name, self.last_name, self.address,
                             # self.home_tel, self.mobile_tel, self.work_tel,
                                                           # self.email, self.email2, self.email3,
                              # self.phone2,
                                                           self.all_phones_from_home_page, self.all_emails)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name\
               and self.last_name==other.last_name and self.address == other.address\
            and self.all_phones_from_home_page == other.all_phones_from_home_page\
            and self.all_emails == other.all_emails


