import time

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def delete_first(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # click Delete button
        wd.find_element_by_xpath("//input[@value='Delete group(s)']").click()
        self.open_group_page()
        time.sleep(3)

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        self.fill_group_fields(group)
        wd.find_element_by_name("submit").click()
        self.open_group_page()

    def fill_group_fields(self, group):
        self.type_in_field("group_name", group.name)
        self.type_in_field("group_header", group.header)
        self.type_in_field("group_footer", group.footer)

    def type_in_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first(self, group):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # click Edit
        wd.find_element_by_name("edit").click()
        self.fill_group_fields(group)
        # click Update button
        wd.find_element_by_name("update").click()
        self.open_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()