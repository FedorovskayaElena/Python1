# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(postfix, maxlen):
    s = "".join([random.choice(string.ascii_letters + string.digits + " "*10) for i in range(random.randrange(maxlen))])
    return s + postfix


# формирование тестовых данных
# вначале первый реальный контакт со всеми заполненными полями, похожими на реальные данные
# затем комбинации пустых/заполненых полей (по всем полям, представленным на главное странице)
# затем несколько контактов со случайно сгенеренными данными (без проверок)
test_data = [Contact(firstname="Ойсеф Ийельский", initials="K.", lastname="Петрещенко", nickname="AllaI",
                     title="Mrs.", company="Nothing", address="Sadovoe 34-34-2", homephone="495 3332211",
                     mobilephone="965 2223344",
                     workphone="965 1112233", fax="965 8889988", email="afel1@mail.ru", email2="afel2@mail.ru",
                     email3="afel3@mail.ru", homepage="www.test.com",
                     bdayoption="option[10]", bmonthoption="option[2]", byear="1980",
                     adayoption="option[17]", amonthoption="option[4]", ayear="2000",
                     address2="Seletor str d. 98 kv.34", phone2="www.home.com", notes="Very important contact",
                     photopath="/Users/lena/Desktop/cat1.jpg")] + \
            [Contact(firstname=firstname, initials=initials, lastname=lastname, address=address)
             for firstname in ["", random_string("firstname", 20)]
             for initials in ["", random_string("initials", 5)]
             for lastname in ["", random_string("lastname", 20)]
             for address in ["", random_string("address", 40)]] + \
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
                     bdayoption="option[10]", bmonthoption="option[2]", byear="1980",
                     adayoption="option[17]", amonthoption="option[4]", ayear="2000",
                     address2=random_string("address2", 20), phone2=random_string("phone2", 20),
                     notes=random_string("notes", 100)) for i in range(5)]


@pytest.mark.parametrize("new_contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, new_contact):
    old_contacts_list = app.contact.get_contacts_list()
    app.contact.create(new_contact)
    assert len(old_contacts_list) + 1 == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    print("\n%s" % old_contacts_list)
    old_contacts_list.append(new_contact)
    print("Appended:\n%s" % old_contacts_list)
    print("Sorted:\n%s\n%s" % (sorted(old_contacts_list, key=Contact.id_or_max), sorted(new_contacts_list, key=Contact.id_or_max)))
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)






