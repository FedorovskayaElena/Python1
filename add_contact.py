# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact
from login import userlogin
import time


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False},
                            firefox_binary="/Applications/Firefox.app/Contents/MacOS/firefox")
        self.wd.implicitly_wait(60)


    def create_contact(self, wd, contact):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.initials)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)

        photoinput = wd.find_element_by_name("photo")
        photoinput.send_keys(contact.photopath)
        time.sleep(3)

        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.workphone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)

        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//" + contact.bdayoption).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//" + contact.bdayoption).click()

        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//" + contact.bmonthoption).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//" + contact.bmonthoption).click()

        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)

        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//" + contact.adayoption).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//" + contact.adayoption).click()

        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//" + contact.amonthoption).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//" + contact.amonthoption).click()

        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)

        if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[1]").click()

        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def tearDown(self):
        self.wd.quit()

    def test_add_contact(self):

        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")
        userlogin(wd, "admin", "secret")

        self.create_contact(wd, Contact(firstname="Aliona 3", initials="K.", lastname="Ivanova", nickname="AllaI",
                           title="Mrs.", company="Nothing", address="Sadovoe 34-34-2", homephone="495 3332211",
                           mobilephone="965 2223344",
                           workphone="965 1112233", fax="965 8889988", email="afel1@mail.ru", email2="afel2@mail.ru",
                           email3="afel3@mail.ru", homepage="www.test.com",
                           bdayoption="option[10]", bmonthoption="option[2]", byear="1980",
                           adayoption="option[17]", amonthoption="option[4]", ayear="2000",
                           address2="Seletor str d. 98 kv.34", phone2="www.home.com", notes="Very important contact",
                                        photopath="/Users/lena/Desktop/cat1.jpg"))

        wd.find_element_by_link_text("Logout").click()


if __name__ == '__main__':
    unittest.main()
