# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group("Added from test_delete", "Header 2", "Footer 2"))
    old_groups_list = app.group.get_groups_list()
    app.group.delete_first()
    assert len(old_groups_list) - 1 == app.group.count()
    new_groups_list = app.group.get_groups_list()
    print("")
    print(old_groups_list)
    print(new_groups_list)
    old_groups_list[0:1] = []
    print("Deleted:")
    print(old_groups_list)
    print("Sorted:")
    print(sorted(old_groups_list, key=lambda gr: gr.group_id))
    print(sorted(new_groups_list,  key=lambda gr: gr.group_id))
    assert sorted(old_groups_list,  key=lambda gr: gr.group_id) == sorted(new_groups_list,  key=lambda gr: gr.group_id)


def test_delete_first_group_1(app):
    if app.group.count() == 0:
        app.group.create(Group("Added from test_delete", "Header 2", "Footer 2"))
    old_groups_list = app.group.get_groups_list()
    app.group.delete_first()
    assert len(old_groups_list) - 1 == app.group.count()
    new_groups_list = app.group.get_groups_list()
    print("")
    print(old_groups_list)
    print(new_groups_list)
    old_groups_list[0:1] = []
    print("Deleted:")
    print(old_groups_list)
    print("Sorted:")
    print(sorted(old_groups_list, key=lambda gr: gr.group_id))
    print(sorted(new_groups_list,  key=lambda gr: gr.group_id))
    assert sorted(old_groups_list,  key=lambda gr: gr.group_id) == sorted(new_groups_list,  key=lambda gr: gr.group_id)
