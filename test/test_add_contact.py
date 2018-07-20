# -*- coding: utf-8 -*-
from model.contact import Contact


# запуск тестовой функции на данных в файле питон
def test_add_contact_module(app, db, data_contacts, check_ui):
    new_contact = data_contacts
    old_contacts_list = db.get_contacts_list()
    app.contact.create(new_contact)
    new_contacts_list = db.get_contacts_list()
    old_contacts_list.append(new_contact)
    # сортируем только старый список, в который сами добавили группу, из базы уже сортированный
    # чистить не надо - они не из интерфейса
    assert sorted(old_contacts_list, key=Contact.id_or_max) == new_contacts_list
    # а вот список из интерфейса надо сортировать
    # и раз в интерфейсе пробелмы чистятся, то лучше и наши оба списка от пробелов почистить
    if check_ui:
        new_contacts_list_cleaned = [c.clean_contact() for c in new_contacts_list]
        ui_contacts_list_cleaned = [c.clean_contact() for c in app.contact.get_contacts_list()]
        assert new_contacts_list_cleaned == sorted(ui_contacts_list_cleaned, key=lambda c: c.id_or_max())
        print("Checked UI")


# запуск тестовой функции на данных в файле JSON
def test_add_contact_json(app, db, json_contacts, check_ui):
    new_contact = json_contacts
    old_contacts_list = db.get_contacts_list()
    app.contact.create(new_contact)
    new_contacts_list = db.get_contacts_list()
    old_contacts_list.append(new_contact)
    # сортируем только старый список, в который сами добавили группу, из базы уже сортированный
    # чистить не надо - они не из интерфейса
    assert sorted(old_contacts_list, key=Contact.id_or_max) == new_contacts_list
    # а вот список из интерфейса надо сортировать
    # и раз в интерфейсе пробелмы чистятся, то лучше и наши оба списка от пробелов почистить
    if check_ui:
        new_contacts_list_cleaned = [c.clean_contact() for c in new_contacts_list]
        ui_contacts_list_cleaned = [c.clean_contact() for c in app.contact.get_contacts_list()]
        assert new_contacts_list_cleaned == sorted(ui_contacts_list_cleaned, key=lambda c: c.id_or_max())
        print("Checked UI")
