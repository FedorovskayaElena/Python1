from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        self.select_contact_by_index(index)
        # click Delete button
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contacts_cache = None
        self.open_contacts_page()

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        self.select_contact_by_id(id)
        # click Delete button
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contacts_cache = None
        self.open_contacts_page()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_fields(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contacts_cache = None
        self.open_contacts_page()

    def create_contact_in_group(self, contact, group):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_fields(contact)
        # выбрать группу с нужным индексом
        wd.find_element_by_xpath("//select[@name='new_group']/option[@value='%s']" % str(group.group_id)).click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contacts_cache = None
        self.open_contacts_page()

    def modify_first(self, contact):
        self.modify_by_index(contact, 0)

    def modify_by_index(self, contact, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # click Edit button
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[%s]/td[8]/a" % str(2 + index)).click()
        self.fill_contact_fields(contact)
        # клик по кнопке Update
        wd.find_element_by_name("update").click()
        self.contacts_cache = None
        self.open_contacts_page()

    def modify_by_id(self, contact, id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
        # click Edit button
        # XPATH в виде //a[@href='edit.php?id=781'] или //input[@value='781']/../../td[8]/a
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % str(id)).click()
        self.fill_contact_fields(contact)
        # клик по кнопке Update
        wd.find_element_by_name("update").click()
        self.contacts_cache = None
        self.open_contacts_page()

    def open_contacts_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/index.php"):
            wd.find_element_by_link_text("home").click()

    def open_view_contact_page(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # click Edit button
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[%s]/td[7]/a" % str(2 + index)).click()

    def open_edit_contact_page(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # click Edit button
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[%s]/td[8]/a" % str(2 + index)).click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='%s']" % str(id)).click()

    def type_in_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_drop_down(self, xpath, selected_value):
        wd = self.app.wd
        if selected_value is not None:
            if not wd.find_element_by_xpath(xpath + selected_value).is_selected():
                wd.find_element_by_xpath(xpath + selected_value).click()

    def fill_contact_fields(self, contact):
        wd = self.app.wd
        self.type_in_field("firstname", contact.firstname)
        self.type_in_field("middlename", contact.initials)
        self.type_in_field("lastname", contact.lastname)
        self.type_in_field("nickname", contact.nickname)
        # photoinput = wd.find_element_by_name("photo")
        # photoinput.send_keys(contact.photopath)
        # self.type_in_field("photo", contact.photopath)
        self.type_in_field("title", contact.title)
        self.type_in_field("company", contact.company)
        self.type_in_field("address", contact.address)
        self.type_in_field("home", contact.homephone)
        self.type_in_field("mobile", contact.mobilephone)
        self.type_in_field("work", contact.workphone)
        self.type_in_field("fax", contact.fax)
        self.type_in_field("email", contact.email)
        self.type_in_field("email2", contact.email2)
        self.type_in_field("email3", contact.email3)
        self.type_in_field("homepage", contact.homepage)
        self.select_drop_down("//div[@id='content']/form/select[1]//", contact.bdayoption)
        self.select_drop_down("//div[@id='content']/form/select[2]//", contact.bmonthoption)
        self.type_in_field("byear", contact.byear)
        self.select_drop_down("//div[@id='content']/form/select[3]//", contact.adayoption)
        self.select_drop_down("//div[@id='content']/form/select[4]//", contact.amonthoption)
        self.type_in_field("ayear", contact.ayear)
        # в редактировании контакта нет поля для выбора группы! добавить проверку есть ли элемент
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[1]").is_selected():
        #    wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[1]").click()
        self.type_in_field("address2", contact.address2)
        self.type_in_field("phone2", contact.phone2)
        self.type_in_field("notes", contact.notes)

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def get_contacts_list(self):
        wd = self.app.wd
        if self.contacts_cache is None:
            self.open_contacts_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                tds = element.find_elements_by_css_selector("td")
                id = tds[0].find_element_by_css_selector("input[name='selected[]']").get_attribute("value")
                last = tds[1].get_attribute("innerText")
                first = tds[2].get_attribute("innerText")
                address = tds[3].get_attribute("innerText")
                all_emails = tds[4].get_attribute("innerText")
                all_phones = tds[5].get_attribute("innerText")
                # print("Contact list ID: %s / Last: %s / First: %s" % (str(id), last, first))
                # print("Contact address %s" % address)
                # print("All phones %s" % all_phones)
                self.contacts_cache.append(Contact(firstname=first, lastname=last, contact_id=id, address=address,
                                                   all_phones_from_homepage=all_phones, all_emails_from_homepage=all_emails))
        return list(self.contacts_cache)

    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_edit_contact_page(index)
        contact = Contact()
        contact.contact_id = wd.find_element_by_name("id").get_attribute("value")
        contact.firstname = wd.find_element_by_name("firstname").get_attribute("value")
        contact.lastname = wd.find_element_by_name("lastname").get_attribute("value")
        contact.address =  wd.find_element_by_name("address").get_attribute("value")
        contact.homephone = wd.find_element_by_name("home").get_attribute("value")
        contact.mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        contact.workphone = wd.find_element_by_name("work").get_attribute("value")
        contact.phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        contact.email = wd.find_element_by_name("email").get_attribute("value")
        contact.email2 = wd.find_element_by_name("email2").get_attribute("value")
        contact.email3 = wd.find_element_by_name("email3").get_attribute("value")
        # print("\nFrom Edit page:\n 1: %s 2: %s / 3:%s" % (contact.email, contact.email2, contact.email3))
        return contact

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_view_contact_page(index)
        content = wd.find_element_by_id("content").text
        contact = Contact()
        contact.contact_id = wd.find_element_by_name("id").get_attribute("value")
        contact.content_from_view_page = re.sub("H:", "", re.search("H: (.*)", content).group(0))
        contact.mobilephone = re.sub("M:", "", re.search("M: (.*)", content).group(0))
        contact.workphone = re.sub("W:", "", re.search("W: (.*)", content).group(0))
        contact.phone2 = re.sub("P:", "", re.search("P: (.*)", content).group(0))
        # print("\nFrom View page:\n ID: %s H: %s / M:%s / W: %s / P: %s" % (contact.contact_id, contact.homephone,
        #                                                                    contact.mobilephone, contact.workphone,
        #                                                                    contact.phone2))
        return contact

    def get_all_content_from_view_page(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_view_contact_page(index)
        contact = Contact()
        contact.contact_id = wd.find_element_by_name("id").get_attribute("value")
        contact.all_content_from_viewpage = wd.find_element_by_id("content").text
        # print("\nID %s:\n Content:\n %s" % (contact.contact_id, contact.all_content_from_viewpage))
        return contact

    def link_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.open_contacts_page()
        # select contact
        self.select_contact_by_id(contact.contact_id)
        # select group
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='%s']" % str(group.group_id)).click()
        # click Add button
        wd.find_element_by_xpath("//input[@value='Add to']").click()
        self.open_contacts_page()

    def delete_contact_from_group(self, contact, group):
        print("Trying to remove\nContact %s\ngroup from %s" % (contact, group))
        wd = self.app.wd
        self.open_contacts_page()
        # select group
        wd.find_element_by_xpath("//select[@name='group']/option[@value='%s']" % str(group.group_id)).click()
        # выбрать нужный контакт на странице контактов выбранной группы
        self.select_contact_by_id(contact.contact_id)
        # click Remove from group button
        wd.find_element_by_xpath("//input[contains(@value, 'Remove from')]").click()
        self.open_contacts_page()
        print("Result:\n Contact %s\nremoved from %s" % (contact, group))