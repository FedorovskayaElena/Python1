def login(wd, username, userpassword):
    # open group page
    wd.get("http://localhost/addressbook/group.php")

    wd.find_element_by_name("user").click()
    wd.find_element_by_name("user").clear()
    wd.find_element_by_name("user").send_keys(username)
    wd.find_element_by_name("pass").click()
    wd.find_element_by_name("pass").clear()
    wd.find_element_by_name("pass").send_keys(userpassword)
    wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


def logout(wd):
    wd.find_element_by_link_text("Logout").click()