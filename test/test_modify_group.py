# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    app.group.modify_first(Group("New Name 111111111111", "New Header", "New Footer"))


def test_modify_group_name(app):
    app.group.modify_first(Group("Absolutely New Name 1", ""))
