import random
import string
import jsonpickle
import os.path
import getopt
import sys

# чтобы при вызове из командной строки было видно модуль model.contact
model_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(model_dir)
from model.contact import Contact


def random_string(postfix, maxlen):
    s = "".join([random.choice(string.ascii_letters + string.digits + " "*10) for i in range(random.randrange(maxlen))])
    return s + postfix


def random_days_months(start, end):
    d = "option[%s]" % random.randrange(start, end)
    return d


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

# вначале первый реальный контакт со всеми заполненными полями, похожими на реальные данные
# затем комбинации пустых/заполненых полей (по всем полям, представленным на главное странице)
# затем несколько контактов со случайно сгенеренными данными
if n == 0:
    test_data = []
else:
    test_data = [Contact(firstname="Ойсеф Ийельский", initials="K.", lastname="Петрещенко", nickname="AllaI",
                     title="Mrs.", company="Nothing", address="Sadovoe 34-34-2", homephone="495 3332211",
                     mobilephone="965 2223344",
                     workphone="965 1112233", fax="965 8889988", email="afel1@mail.ru", email2="afel2@mail.ru",
                     email3="afel3@mail.ru", homepage="www.test.com",
                     bdayoption="option[10]", bmonthoption="option[2]", byear="1980",
                     adayoption="option[17]", amonthoption="option[4]", ayear="2000",
                     address2="Seletor str d. 98 kv.34", phone2="www.home.com", notes="Very important contact",
                     photopath="/Users/lena/Desktop/cat1.jpg")] + \
            [Contact(firstname=random_string("firstname", 20), initials=random_string("initials", 20),
                     lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
                     title="Mrs.", company=random_string("company", 20),
                     address=random_string("address", 20),
                     homephone=random_string("homephone", 20),
                     mobilephone=random_string("mobilephone", 20),
                     workphone=random_string("workphone", 20),
                     fax=random_string("fax", 20),
                     email=random_string("email", 20), email2=random_string("email2", 20),
                     email3=random_string("email3", 20), homepage=random_string("homepage", 20),
                     bdayoption=random_days_months(1, 32), bmonthoption=random_days_months(1, 14), byear=random_string("", 4),
                     adayoption=random_days_months(1, 32), amonthoption=random_days_months(1, 14), ayear=random_string("", 4),
                     address2=random_string("address2", 20), phone2=random_string("phone2", 20),
                     notes=random_string("notes", 100)) for i in range(n-1)]


file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file_name, "w") as file:
    jsonpickle.set_encoder_options("json", indent=2, ensure_ascii=False)
    file.write(jsonpickle.encode(test_data))

