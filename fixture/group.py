from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # click Delete button
        wd.find_element_by_xpath("//input[@value='Delete group(s)']").click()
        self.group_cache = None
        self.open_groups_page()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_group_fields(group)
        wd.find_element_by_name("submit").click()
        self.group_cache = None
        self.open_groups_page()

    def modify_first(self, group):
        self.modify_by_index(group, 0)

    def modify_by_index(self, group, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # click Edit
        wd.find_element_by_name("edit").click()
        self.fill_group_fields(group)
        # click Update button
        wd.find_element_by_name("update").click()
        self.group_cache = None
        self.open_groups_page()

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

    def select_first_group(self):
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_groups_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector('span.group'):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, group_id=id))
        return list(self.group_cache)


