from sys import maxsize
from model.technical import clear_extra_spaces


class Contact:
    def __init__(self, firstname=None, initials=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, fax=None,
                 email=None, email2=None, email3=None, homepage=None,
                 bdayoption=None, bmonthoption=None, byear=None, adayoption=None, amonthoption=None, ayear=None,
                 address2=None, phone2=None, notes=None, photopath=None, contact_id=None,
                 all_phones_from_homepage=None, all_emails_from_homepage=None, all_content_from_viewpage=None):
        self.firstname = firstname
        self.initials = initials
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bdayoption = bdayoption
        self.bmonthoption = bmonthoption
        self.byear = byear
        self.adayoption = adayoption
        self.amonthoption = amonthoption
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.photopath = photopath
        self.contact_id = contact_id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage
        self.all_content_from_viewpage = all_content_from_viewpage

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None or str(self.contact_id) == str(other.contact_id)) and \
               clear_extra_spaces(self.firstname) == clear_extra_spaces(other.firstname) and \
               clear_extra_spaces(self.lastname) == clear_extra_spaces(other.lastname)

    def __repr__(self):
        return "ID:%s/FN:%s/LN:%s" % (self.contact_id, self.firstname, self.lastname)

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize

    def clean_contact(self, id_transfer_to_int=False):
        if self.firstname is not None:
            self.firstname = clear_extra_spaces(self.firstname)
        if self.lastname is not None:
            self.lastname = clear_extra_spaces(self.lastname)
        if self.address is not None:
            self.address = clear_extra_spaces(self.address)
        if self.email is not None:
            self.email = clear_extra_spaces(self.email)
        if self.email2 is not None:
            self.email2 = clear_extra_spaces(self.email2)
        if self.email3 is not None:
            self.email3 = clear_extra_spaces(self.email3)
        if self.homephone is not None:
            self.homephone = clear_extra_spaces(self.homephone)
        if self.mobilephone is not None:
            self.mobilephone = clear_extra_spaces(self.mobilephone)
        if self.workphone is not None:
            self.workphone = clear_extra_spaces(self.workphone)
        if self.phone2 is not None:
            self.phone2 = clear_extra_spaces(self.phone2)

        if id_transfer_to_int:
            self.contact_id = int(self.contact_id)
        return self



