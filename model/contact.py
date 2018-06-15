from sys import maxsize


class Contact:
    def __init__(self, firstname=None, initials=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, fax=None,
                 email=None, email2=None, email3=None, homepage=None,
                 bdayoption=None, bmonthoption=None, byear=None, adayoption=None, amonthoption=None, ayear=None,
                 address2=None, phone2=None, notes=None, photopath=None, contact_id=None):
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

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id) and \
               self.firstname == other.firstname and self.lastname == other.lastname

    def __repr__(self):
        return "%s: %s %s" % (self.contact_id, self.firstname, self.lastname)

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize

