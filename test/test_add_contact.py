# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import time


def test_open_page(app):
    time.sleep(3)
    app.contact.open_view_contact_page(app.contact.count()-1)
    time.sleep(3)
    app.contact.open_edit_contact_page(app.contact.count() - 1)
    time.sleep(3)


def test_add_contact(app):
    old_contacts_list = app.contact.get_contacts_list()
    new_contact = Contact(firstname="Ойсеф Ийельский", initials="K.", lastname="Петрещенко", nickname="AllaI",
                           title="Mrs.", company="Nothing", address="Sadovoe 34-34-2", homephone="495 3332211",
                           mobilephone="965 2223344",
                           workphone="965 1112233", fax="965 8889988", email="afel1@mail.ru", email2="afel2@mail.ru",
                           email3="afel3@mail.ru", homepage="www.test.com",
                           bdayoption="option[10]", bmonthoption="option[2]", byear="1980",
                           adayoption="option[17]", amonthoption="option[4]", ayear="2000",
                           address2="Seletor str d. 98 kv.34", phone2="www.home.com", notes="Very important contact",
                                        photopath="/Users/lena/Desktop/cat1.jpg")
    app.contact.create(new_contact)
    assert len(old_contacts_list) + 1 == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    print("\n%s" % old_contacts_list)
    old_contacts_list.append(new_contact)
    print("Appended:\n%s" % old_contacts_list)
    print("Sorted:\n%s\n%s" % (sorted(old_contacts_list, key=Contact.id_or_max), sorted(new_contacts_list, key=Contact.id_or_max)))
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)


def test_add_contact_1(app):
    old_contacts_list = app.contact.get_contacts_list()
    new_contact = Contact(firstname="Сыр", initials="K.", lastname="Сырников", nickname="AllaI",
                           title="Mrs.", company="Nothing", address="Sadovoe 34-34-2", homephone="495 3332211",
                           mobilephone="965 2223344",
                           workphone="965 1112233", fax="965 8889988", email="afel1@mail.ru", email2="afel2@mail.ru",
                           email3="afel3@mail.ru", homepage="www.test.com",
                           bdayoption="option[10]", bmonthoption="option[2]", byear="1980",
                           adayoption="option[17]", amonthoption="option[4]", ayear="2000",
                           address2="Seletor str d. 98 kv.34", phone2="www.home.com", notes="Very important contact",
                                        photopath="/Users/lena/Desktop/cat1.jpg")
    app.contact.create(new_contact)
    assert len(old_contacts_list) + 1 == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    print("\n%s" % old_contacts_list)
    old_contacts_list.append(new_contact)
    print("Appended:\n%s" % old_contacts_list)
    print("Sorted:\n%s\n%s" % (sorted(old_contacts_list, key=Contact.id_or_max), sorted(new_contacts_list, key=Contact.id_or_max)))
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)




