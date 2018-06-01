# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group
from login import userlogin

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

    def create_group(self, wd, group):
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


    def test_add_group(self):
        wd = self.wd
        # open group page
        wd.get("http://localhost/addressbook/group.php")
        userlogin(wd, "admin", "secret")
        self.create_group(wd, Group("Name 2", "Header 2", "Footer 2"))
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("Logout").click()
    

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
