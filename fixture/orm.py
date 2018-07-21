from pony.orm import *
from _datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import encoders, decoders, convert_mysql_timestamp


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        group_id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        contact_id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        address = Optional(str, column='address')
        homephone = Optional(str, column='home')
        workphone = Optional(str, column='mobile')
        mobilephone = Optional(str, column='work')
        phone2 = Optional(str, column='phone2')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        deprecated = Optional(str, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts', lazy=True)

    def __init__(self, host, database, user, password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql', host=host, database=database, user=user, password=password, conv=conv)
        self.db.generate_mapping()
        sql_debug(True)

    @db_session
    def get_group_list_with_non_empty_names(self):
        orm_groups = list(select(g for g in ORMFixture.ORMGroup if g.name != ''))
        return self.convert_groups_to_model(orm_groups)

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(list(select(c for c in ORMFixture.ORMContact if c.deprecated is None)))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.group_id == group.group_id))[0]
        orm_contacts = list(select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group in c.groups))
        return self.convert_contacts_to_model(orm_contacts)

    #  достаем группы с непустыми именами, потому что у пустых нет кнопки Remove from
    @db_session
    def get_groups_with_contacts_and_non_empty_names(self):
        orm_groups = select(g for g in ORMFixture.ORMGroup if g.contacts)
        return self.convert_groups_to_model(orm_groups.filter(lambda p: p.name != ''))

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(group_id=str(group.group_id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(contact_id=str(contact.contact_id), firstname=contact.firstname, lastname=contact.lastname,
                           address=contact.address, homephone=contact.homephone, workphone=contact.workphone,
                           mobilephone=contact.mobilephone, phone2=contact.phone2, email=contact.email,
                           email2=contact.email2, email3=contact.email3)
        return list(map(convert, contacts))

    @db_session
    def find_contact_in_group(self, contact, group):
        orm_groups = list(select(g for g in ORMFixture.ORMGroup if g.group_id == group.group_id))[0]
        contacts = self.convert_contacts_to_model(orm_groups.contacts)
        return contact in contacts
