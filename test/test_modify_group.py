# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group("AAAAdded from test_modify", "Header 2", "Footer 2"))
    app.group.modify_first(Group("New Name 111111111111", "New Header", "New Footer"))


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group("AAAAdded from test_modify_group_name", "Header 2", "Footer 2"))
    app.group.modify_first(Group("Absolutely New Name 1"))
