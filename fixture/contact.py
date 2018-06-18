import time
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def delete_first(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        self.select_first_contact()
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
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        self.select_first_contact()
        # click Edit button
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_fields(contact)
        # клик по кнопке Update
        wd.find_element_by_name("update").click()
        self.contacts_cache = None
        self.open_contacts_page()

    def open_contacts_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/index.php"):
            wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

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
                textid = element.find_element_by_css_selector("td>input[name='selected[]']").get_attribute("value")
                textlast = element.find_element_by_css_selector("td+td").get_attribute("innerText")
                textfirst = element.find_element_by_css_selector("td+td+td").get_attribute("innerText")
                # print("ok")
                # print("ID:" + textid)
                # print("Last:" + textlast)
                # print("First:" + textfirst)
                self.contacts_cache.append(Contact(firstname=textfirst, lastname=textlast, contact_id=textid))
        return list(self.contacts_cache)


