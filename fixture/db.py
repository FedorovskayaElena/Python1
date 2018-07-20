import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DBFixture:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=database, user=user, password=password)
        self.connection.autocommit(True)

    def destroy(self):
        self.connection.close()

    def get_groups_list(self):
        cursor = self.connection.cursor()
        groups = []
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                groups.append(Group(group_id=int(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return groups

    def get_contacts_list(self):
        cursor = self.connection.cursor()
        contacts = []
        try:
            cursor.execute("select id, lastname, firstname, address, email, email2, email3, home, mobile, work, phone2 "
                           "from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, lastname, firstname, address, email, email2, email3, home, mobile, work, phone2) = row
                contacts.append(Contact(contact_id=int(id), firstname=firstname, lastname=lastname, address=address,
                                      email=email, email2=email2, email3=email3,
                                      homephone=home, mobilephone=mobile, workphone=work, phone2=phone2))
        finally:
            cursor.close()
        return contacts
