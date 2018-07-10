# -*- coding: utf-8 -*-
from model.contact import Contact


# запуск тестовой функции на данных в файле питон
def test_add_contact_module(app, data_contacts):
    new_contact = data_contacts
    old_contacts_list = app.contact.get_contacts_list()
    app.contact.create(new_contact)
    assert len(old_contacts_list) + 1 == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    # print("\n%s %s", (new_contact.bdayoption, new_contact.bmonthoption))
    # print("\n%s %s", (new_contact.bdayoption, new_contact.bmonthoption))
    old_contacts_list.append(new_contact)
    # print("Appended:\n%s" % old_contacts_list)
    # print("Sorted:\n%s\n%s" % (sorted(old_contacts_list, key=Contact.id_or_max), sorted(new_contacts_list, key=Contact.id_or_max)))
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)


# запуск тестовой функции на данных в файле JSON
def test_add_contact_json(app, json_contacts):
    new_contact = json_contacts
    old_contacts_list = app.contact.get_contacts_list()
    app.contact.create(new_contact)
    assert len(old_contacts_list) + 1 == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    # print("\n%s %s", (new_contact.bdayoption, new_contact.bmonthoption))
    # print("\n%s %s", (new_contact.bdayoption, new_contact.bmonthoption))
    old_contacts_list.append(new_contact)
    # print("Appended:\n%s" % old_contacts_list)
    # print("Sorted:\n%s\n%s" % (sorted(old_contacts_list, key=Contact.id_or_max), sorted(new_contacts_list, key=Contact.id_or_max)))
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)