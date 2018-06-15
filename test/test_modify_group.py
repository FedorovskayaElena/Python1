# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group("Added from test_modify", "Header 2", "Footer 2"))
    old_groups_list = app.group.get_groups_list()
    new_group = Group(name="Modified #3", group_id=old_groups_list[0].group_id)
    app.group.modify_first(new_group)
    new_groups_list = app.group.get_groups_list()
    print("")
    print(old_groups_list)
    print(new_groups_list)
    assert len(old_groups_list) == len(new_groups_list)
    old_groups_list[0] = new_group
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
