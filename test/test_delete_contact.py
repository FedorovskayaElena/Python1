# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import pytest


test_data = [i for i in range(10)]


@pytest.mark.parametrize("number", test_data)
def test_delete_contact(app, number):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Марина Added from test_delete", lastname="Петрова",
                           title="Mrs.", company="Nothing", address="Sadovoe 34-34-2", homephone="495 3332211",
                           mobilephone="965 2223344",
                           workphone="965 1112233", fax="965 8889988"))
    old_contacts_list = app.contact.get_contacts_list()
    delete_index = randrange(len(old_contacts_list))
    print("Random index 1: %s" % str(delete_index))
    app.contact.delete_by_index(delete_index)
    assert len(old_contacts_list) - 1 == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    print("\n%s\n%s" % (old_contacts_list, new_contacts_list))
    old_contacts_list[delete_index:delete_index+1] = []
    print("Deleted:\n%s" % old_contacts_list)
    print("Sorted:\n%s\n%s" % (sorted(old_contacts_list, key=lambda gr: gr.contact_id),
                               sorted(new_contacts_list,  key=lambda gr: gr.contact_id)))
    assert sorted(old_contacts_list,  key=lambda gr: gr.contact_id) == sorted(new_contacts_list,  key=lambda gr: gr.contact_id)



