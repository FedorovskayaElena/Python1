# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Марина Added from test_delete", lastname="Петрова",
                           title="Mrs.", company="Nothing", address="Sadovoe 34-34-2", homephone="495 3332211",
                           mobilephone="965 2223344",
                           workphone="965 1112233", fax="965 8889988"))
    old_contacts_list = app.contact.get_contacts_list()
    app.contact.delete_first()
    new_contacts_list = app.contact.get_contacts_list()
    print("")
    print(old_contacts_list)
    print(new_contacts_list)
    assert len(old_contacts_list) - 1 == len(new_contacts_list)
    old_contacts_list[0:1] = []
    print("Deleted:")
    print(old_contacts_list)
    print("Sorted:")
    print(sorted(old_contacts_list, key=lambda gr: gr.contact_id))
    print(sorted(new_contacts_list,  key=lambda gr: gr.contact_id))
    assert sorted(old_contacts_list,  key=lambda gr: gr.contact_id) == sorted(new_contacts_list,  key=lambda gr: gr.contact_id)
