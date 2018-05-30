def userlogin(wd, username, userpassword):
    wd.find_element_by_name("user").click()
    wd.find_element_by_name("user").clear()
    wd.find_element_by_name("user").send_keys(username)
    wd.find_element_by_name("pass").click()
    wd.find_element_by_name("pass").clear()
    wd.find_element_by_name("pass").send_keys(userpassword)
    wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()