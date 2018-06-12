# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group("Group Added from test_delete", "Header 2", "Footer 2"))
    app.group.delete_first()
