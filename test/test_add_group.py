# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("Name", "Header 2", "Footer 2"))
    app.session.logout()
