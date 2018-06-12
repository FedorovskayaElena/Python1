# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group("AaaName #1", "Header 2", "Footer 2"))


def test_add_group_1(app):
    app.group.create(Group("AAAName #2", "Header 2", "Footer 2"))