# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group("Name 001", "Header 2", "Footer 2"))


def test_add_group_1(app):
    app.group.create(Group("Name 002", "Header 2", "Footer 2"))