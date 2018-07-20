# -*- coding: utf-8 -*-
from model.contact import Contact
from random import choice
import pytest


test_data = [i for i in range(3)]


@pytest.mark.parametrize("number", test_data)
def test_delete_contact(app, db, number, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Марина Added from test_delete", lastname="Петрова",
                           title="Mrs.", company="Nothing", address="Sadovoe 34-34-2", homephone="495 3332211",
                           mobilephone="965 2223344",
                           workphone="965 1112233", fax="965 8889988"))
    old_contacts_list = db.get_contacts_list()
    delete_contact = choice(old_contacts_list)
    print("Random index 1: %s" % str(delete_contact.contact_id))
    app.contact.delete_by_id(delete_contact.contact_id)
    new_contacts_list = db.get_contacts_list()
    print("\n%s\n%s" % (old_contacts_list, new_contacts_list))
    old_contacts_list.remove(delete_contact)
    print("Deleted:\n%s" % old_contacts_list)
    assert old_contacts_list == new_contacts_list
    if check_ui:
        assert new_contacts_list == sorted(app.contact.get_contacts_list(), key=lambda c: c.id_or_max())
        print("check UI")



