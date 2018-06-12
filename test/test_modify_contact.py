# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Revv Марина Added from test_modify", lastname="Петрова",
                           title="Mrs.", company="Nothing", address="Sadovoe 34-34-2", homephone="495 3332211",
                           mobilephone="965 2223344",
                           workphone="965 1112233", fax="965 8889988"))
    app.contact.modify_first(Contact(firstname="Not Aliona 1", initials="Not K.", lastname="Not Ivanova", nickname="Not AllaI",
                           title="Not Mrs.", company="Not Nothing", address="Not Sadovoe 34-34-2", homephone="495 0000000",
                           mobilephone="965 0000000",
                           workphone="965 0000000", fax="965 0000000", email="n_afel1@mail.ru", email2="n_afel2@mail.ru",
                           email3="n_afel3@mail.ru", homepage="www.n_test.com",
                           bdayoption="option[13]", bmonthoption="option[4]", byear="1981",
                           adayoption="option[14]", amonthoption="option[5]", ayear="2001",
                           address2="not Seletor str d. 98 kv.34", phone2="www.n_home.com", notes="Not Very important contact",
                                        photopath="/Users/lena/Desktop/cat5.jpg"))


def test_modify_contact_somefields(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Марина Added from test_modify_somefields", lastname="Петрова",
                           title="Mrs.", company="Nothing", address="Sadovoe 34-34-2", homephone="495 3332211",
                           mobilephone="965 2223344",
                           workphone="965 1112233", fax="965 8889988"))
    app.contact.modify_first(Contact(lastname="New Petrova", mobilephone="", workphone=""))
