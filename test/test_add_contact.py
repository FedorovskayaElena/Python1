# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):

    app.session.login("admin", "secret")

    app.contact.create(Contact(firstname="Aliona 3", initials="K.", lastname="Ivanova", nickname="AllaI",
                           title="Mrs.", company="Nothing", address="Sadovoe 34-34-2", homephone="495 3332211",
                           mobilephone="965 2223344",
                           workphone="965 1112233", fax="965 8889988", email="afel1@mail.ru", email2="afel2@mail.ru",
                           email3="afel3@mail.ru", homepage="www.test.com",
                           bdayoption="option[10]", bmonthoption="option[2]", byear="1980",
                           adayoption="option[17]", amonthoption="option[4]", ayear="2000",
                           address2="Seletor str d. 98 kv.34", phone2="www.home.com", notes="Very important contact",
                                        photopath="/Users/lena/Desktop/cat1.jpg"))

    app.session.logout()



