# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group
from application import Application


class add_group_1(unittest.TestCase):

    def setUp(self):
        self.app = Application()


    def test_add_group(self):
        self.app.login("admin", "secret")
        self.app.create_group(Group("Name", "Header 2", "Footer 2"))
        self.app.logout()
    

    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
