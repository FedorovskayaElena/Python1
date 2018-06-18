# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups_list = app.group.get_groups_list()
    new_group = Group("B tot 4", "Header 2", "Footer 2")
    app.group.create(new_group)
    assert len(old_groups_list) + 1 == app.group.count()
    new_groups_list = app.group.get_groups_list()
    print("")
    print(old_groups_list)
    print(new_groups_list)
    old_groups_list.append(new_group)
    print("Appended:")
    print(old_groups_list)
    print("Sorted:")
    print(sorted(old_groups_list, key=Group.id_or_max))
    print(sorted(new_groups_list, key=Group.id_or_max))
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)


def test_add_group_1(app):
    old_groups_list = app.group.get_groups_list()
    new_group = Group("Запуск №4444444", "Header 2", "Footer 2")
    app.group.create(new_group)
    assert len(old_groups_list) + 1 == app.group.count()
    new_groups_list = app.group.get_groups_list()
    print("")
    print(old_groups_list)
    print(new_groups_list)
    old_groups_list.append(new_group)
    print("Appended:")
    print(old_groups_list)
    print("Sorted:")
    print(sorted(old_groups_list, key=Group.id_or_max))
    print(sorted(new_groups_list, key=Group.id_or_max))
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)

