# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups_list = app.group.get_groups_list()
    new_group = Group("Abb #1", "Header 2", "Footer 2")
    app.group.create(new_group)
    new_groups_list = app.group.get_groups_list()
    assert len(old_groups_list) + 1 == len(new_groups_list)
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

# def test_add_group_1(app):
#     app.group.create(Group("AAAName #2", "Header 2", "Footer 2"))
