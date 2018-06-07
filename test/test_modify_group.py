# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group(app):
    app.session.login("admin", "secret")
    app.group.modify_first(Group("New Name", "New Header", "New Footer"))
    app.session.logout()
