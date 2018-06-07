# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.session.login("admin", "secret")
    app.contact.modify_first(Contact(firstname="Not Aliona any more", initials="Not K.", lastname="Not Ivanova", nickname="Not AllaI",
                           title="Not Mrs.", company="Not Nothing", address="Not Sadovoe 34-34-2", homephone="495 0000000",
                           mobilephone="965 0000000",
                           workphone="965 0000000", fax="965 0000000", email="n_afel1@mail.ru", email2="n_afel2@mail.ru",
                           email3="n_afel3@mail.ru", homepage="www.n_test.com",
                           bdayoption="option[11]", bmonthoption="option[3]", byear="1981",
                           adayoption="option[11]", amonthoption="option[3]", ayear="2001",
                           address2="not Seletor str d. 98 kv.34", phone2="www.n_home.com", notes="Not Very important contact",
                                        photopath="/Users/lena/Desktop/cat5.jpg"))
    app.session.logout()