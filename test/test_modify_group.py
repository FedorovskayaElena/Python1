# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group("Added from test_modify", "Header 2", "Footer 2"))
    old_groups_list = app.group.get_groups_list()
    modify_index = randrange(len(old_groups_list))
    print("Random index 1: " + str(modify_index))
    new_group = Group(name="Измененная 1", group_id=old_groups_list[modify_index].group_id)
    app.group.modify_by_index(new_group, modify_index)
    assert len(old_groups_list) == app.group.count()
    new_groups_list = app.group.get_groups_list()
    print("")
    print(old_groups_list)
    print(new_groups_list)
    old_groups_list[modify_index] = new_group
    print("Modified:")
    print(old_groups_list)
    print("Sorted:")
    print(sorted(old_groups_list, key=lambda g: g.group_id))
    print(sorted(new_groups_list, key=lambda g: g.group_id))
    assert sorted(old_groups_list, key=lambda g: g.group_id) == sorted(new_groups_list, key=lambda g: g.group_id)


def test_modify_group_1(app):
    if app.group.count() == 0:
        app.group.create(Group("Added from test_modify", "Header 2", "Footer 2"))
    old_groups_list = app.group.get_groups_list()
    modify_index = randrange(len(old_groups_list))
    print("Random index 2: " + str(modify_index))
    new_group = Group(name="Измененная 2", group_id=old_groups_list[modify_index].group_id)
    app.group.modify_by_index(new_group, modify_index)
    assert len(old_groups_list) == app.group.count()
    new_groups_list = app.group.get_groups_list()
    print("")
    print(old_groups_list)
    print(new_groups_list)
    old_groups_list[modify_index] = new_group
    print("Modified:")
    print(old_groups_list)
    print("Sorted:")
    print(sorted(old_groups_list, key=lambda g: g.group_id))
    print(sorted(new_groups_list, key=lambda g: g.group_id))
    assert sorted(old_groups_list, key=lambda g: g.group_id) == sorted(new_groups_list, key=lambda g: g.group_id)

# def test_modify_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group("AAAAdded from test_modify_group_name", "Header 2", "Footer 2"))
#     app.group.modify_first(Group("Absolutely New Name 1"))
