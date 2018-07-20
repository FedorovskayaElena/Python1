# -*- coding: utf-8 -*-
from model.contact import Contact
from random import choice
import pytest


test_data = [i for i in range(2)]


@pytest.mark.parametrize("number", test_data)
def test_modify_contact(app, db, number, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Revv Марина Added from test_modify", lastname="Петрова",
                           title="Mrs.", company="Nothing", address="Sadovoe 34-34-2", homephone="495 3332211",
                           mobilephone="965 2223344",
                           workphone="965 1112233", fax="965 8889988"))
    old_contacts_list = db.get_contacts_list()
    modified_contact = choice(old_contacts_list)
    print("Random index: %s" % str(modified_contact.contact_id))
    new_contact_fields = Contact(firstname="Четверговое имя   %s" % str(number), contact_id=modified_contact.contact_id)
    app.contact.modify_by_id(new_contact_fields, modified_contact.contact_id)
    new_contacts_list = db.get_contacts_list()

    modify_index = old_contacts_list.index(modified_contact)
    old_contacts_list[modify_index].firstname = new_contact_fields.firstname

    #  сортируем только список, который сами модифицировали
    assert sorted(old_contacts_list, key=lambda g: g.contact_id) == new_contacts_list
    # а вот список из интерфейса надо сортировать
    # и раз в интерфейсе пробелмы чистятся, то лучше и наши оба списка от пробелов почистить
    if check_ui:
        new_contacts_list_cleaned = [c.clean_contact() for c in new_contacts_list]
        ui_contacts_list_cleaned = [c.clean_contact() for c in app.contact.get_contacts_list()]
        assert new_contacts_list_cleaned == sorted(ui_contacts_list_cleaned, key=lambda c: c.id_or_max())
        print("Checked UI")


# def test_modify_contact_all_fields(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Марина Added from test_modify_somefields", lastname="Петрова",
#                            title="Mrs.", company="Nothing", address="Sadovoe 34-34-2", homephone="495 3332211",
#                            mobilephone="965 2223344",
#                            workphone="965 1112233", fax="965 8889988"))
#     app.contact.modify_first(Contact(firstname="Not Aliona 1", initials="Not K.", lastname="Not Ivanova", nickname="Not AllaI",
#                            title="Not Mrs.", company="Not Nothing", address="Not Sadovoe 34-34-2", homephone="495 0000000",
#                            mobilephone="965 0000000",
#                            workphone="965 0000000", fax="965 0000000", email="n_afel1@mail.ru", email2="n_afel2@mail.ru",
#                            email3="n_afel3@mail.ru", homepage="www.n_test.com",
#                            bdayoption="option[13]", bmonthoption="option[4]", byear="1981",
#                            adayoption="option[14]", amonthoption="option[5]", ayear="2001",
#                            address2="not Seletor str d. 98 kv.34", phone2="www.n_home.com", notes="Not Very important contact",
#                                         photopath="/Users/lena/Desktop/cat5.jpg"))