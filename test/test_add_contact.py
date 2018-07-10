# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest


@pytest.mark.parametrize("new_contact", test_data1, ids=[repr(x) for x in test_data1])
def test_add_contact(app, new_contact):
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

