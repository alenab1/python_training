import string
import random
import os
from model.contact import Contact
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as e:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "* 25
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", last_name="",
                    home_tel="", work_tel="", mobile_tel="", email="", email2="", email3="",
                    address="", phone2="")] + [
    Contact(first_name=random_string("first_name ", 10), last_name=random_string("last_name ", 10),
                    home_tel=random_string("home_tel ", 10), work_tel=random_string("work_tel ", 10),
                    mobile_tel=random_string("mobile_tel ", 10), email=random_string("email ", 10),
                    email2=random_string("email2 ", 10), email3=random_string("email3 ", 10),
                    address=random_string("address ", 10), phone2=random_string("phone2 ", 10)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as outfile:
    outfile.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))