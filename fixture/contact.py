import time
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
        time.sleep(1)
        wd.switch_to_alert().accept()
        time.sleep(1)
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
                textid = tds[0].find_element_by_css_selector("input[name='selected[]']").get_attribute("value")
                textlast = tds[1].get_attribute("innerText")
                textfirst = tds[2].get_attribute("innerText")
                phones = re.split("\n", tds[5].get_attribute("innerText"))
                homephone = phones[0]
                mobilephone = phones[1]
                workphone = phones[2]
                phone2 = phones[3]
                # print("Contact list ID: %s / Last: %s / First: %s" % (str(textid), textlast, textfirst))
                # print("Home: %s / Mobile: %s / Work: %s / Phone2 %s" % (homephone, mobilephone, workphone, phone2))
                self.contacts_cache.append(Contact(firstname=textfirst, lastname=textlast, contact_id=textid,
                                                   homephone=homephone, mobilephone=mobilephone,
                                                   workphone=workphone, phone2=phone2))
        return list(self.contacts_cache)

    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_edit_contact_page(index)
        contact = Contact()
        contact.contact_id = wd.find_element_by_name("id").get_attribute("value")
        contact.firstname = wd.find_element_by_name("firstname").get_attribute("value")
        contact.lastname = wd.find_element_by_name("lastname").get_attribute("value")
        contact.homephone = wd.find_element_by_name("home").get_attribute("value")
        contact.mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        contact.workphone = wd.find_element_by_name("work").get_attribute("value")
        contact.phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        print("\nFrom Edit page:\n ID: %s H: %s / M:%s / W: %s / P: %s" % (contact.contact_id, contact.homephone,
                                                                           contact.mobilephone, contact.workphone,
                                                                           contact.phone2))
        return contact

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_view_contact_page(index)
        content = wd.find_element_by_id("content").text
        contact = Contact()
        contact.contact_id = wd.find_element_by_name("id").get_attribute("value")
        contact.homephone = re.sub("H:", "", re.search("H: (.*)", content).group(0))
        contact.mobilephone = re.sub("M:", "", re.search("M: (.*)", content).group(0))
        contact.workphone = re.sub("W:", "", re.search("W: (.*)", content).group(0))
        contact.phone2 = re.sub("P:", "", re.search("P: (.*)", content).group(0))
        print("\nFrom View page:\n ID: %s H: %s / M:%s / W: %s / P: %s" % (contact.contact_id, contact.homephone,
                                                                           contact.mobilephone, contact.workphone,
                                                                           contact.phone2))
        return contact


    # def print_css_locator(self):
    #     wd = self.app.wd
    #     elements = wd.find_elements_by_css_selector("tr[name='entry']")
    #     print(elements[0].find_element_by_css_selector("td:nth-child(7) > a").get_attribute("href"))