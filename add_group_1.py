# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class add_group_1(unittest.TestCase):

    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False}, firefox_binary="/Applications/Firefox.app/Contents/MacOS/firefox")
        self.wd.implicitly_wait(60)


    def login(self, username, userpassword):
        wd = self.wd
        # open group page
        wd.get("http://localhost/addressbook/group.php")
        # set username and password
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(userpassword)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()


    def create_group(self, group):
        wd = self.wd

        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()

    def test_add_group(self):
        self.login("admin", "secret")
        self.create_group(Group("Name 2", "Header 2", "Footer 2"))
        self.logout()
    

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
