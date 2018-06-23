import re
import random


def clear(tel):
    cleared_tel = re.sub("[., \-()+]", "", tel)
    return cleared_tel


def test_phones_on_home_page(app):
    index = random.randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    print("\n%s == %s" % (contact_from_home_page.firstname, contact_from_edit_page.firstname))
    print("\n%s == %s" % (contact_from_home_page.lastname, contact_from_edit_page.lastname))
    print("\n%s == %s" % (clear(contact_from_home_page.homephone), clear(contact_from_edit_page.homephone)))
    print("\n%s == %s" % (clear(contact_from_home_page.mobilephone), clear(contact_from_edit_page.mobilephone)))
    print("\n%s == %s" % (clear(contact_from_home_page.workphone), clear(contact_from_edit_page.workphone)))
    print("\n%s == %s" % (clear(contact_from_home_page.phone2), clear(contact_from_edit_page.phone2)))

    assert contact_from_home_page.contact_id == contact_from_edit_page.contact_id
    assert clear(contact_from_home_page.homephone) == clear(contact_from_edit_page.homephone)
    assert clear(contact_from_home_page.mobilephone) == clear(contact_from_edit_page.mobilephone)
    assert clear(contact_from_home_page.workphone) == clear(contact_from_edit_page.workphone)
    assert clear(contact_from_home_page.phone2) == clear(contact_from_edit_page.phone2)


def test_phones_on_view_page(app):
    index = random.randrange(app.contact.count())
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    print("\n%s %s" % (contact_from_edit_page.firstname, contact_from_edit_page.lastname))
    print("\n%s == %s" % (clear(contact_from_view_page.homephone), clear(contact_from_edit_page.homephone)))
    print("\n%s == %s" % (clear(contact_from_view_page.mobilephone), clear(contact_from_edit_page.mobilephone)))
    print("\n%s == %s" % (clear(contact_from_view_page.workphone), clear(contact_from_edit_page.workphone)))
    print("\n%s == %s" % (clear(contact_from_view_page.phone2), clear(contact_from_edit_page.phone2)))

    assert contact_from_view_page.contact_id == contact_from_edit_page.contact_id
    assert clear(contact_from_view_page.homephone) == clear(contact_from_edit_page.homephone)
    assert clear(contact_from_view_page.mobilephone) == clear(contact_from_edit_page.mobilephone)
    assert clear(contact_from_view_page.workphone) == clear(contact_from_edit_page.workphone)
    assert clear(contact_from_view_page.phone2) == clear(contact_from_edit_page.phone2)

