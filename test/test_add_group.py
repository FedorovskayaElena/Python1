# -*- coding: utf-8 -*-
from model.group import Group


# запуск тестовой функции на данных в файле питон
def test_add_group_module(app, data_groups):
    new_group = data_groups
    old_groups_list = app.group.get_groups_list()
    app.group.create(new_group)
    assert len(old_groups_list) + 1 == app.group.count()
    new_groups_list = app.group.get_groups_list()
    # print("\n%s\n%s" % (old_groups_list, new_groups_list))
    old_groups_list.append(new_group)
    # print("Appended:%s" % old_groups_list)
    # print("%s\n%s" % (sorted(old_groups_list, key=Group.id_or_max), sorted(new_groups_list, key=Group.id_or_max)))
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)


# запуск тестовой функции на данных в файле JSON
def test_add_group_json(app, json_groups):
    new_group = json_groups
    old_groups_list = app.group.get_groups_list()
    app.group.create(new_group)
    assert len(old_groups_list) + 1 == app.group.count()
    new_groups_list = app.group.get_groups_list()
    # print("\n%s\n%s" % (old_groups_list, new_groups_list))
    old_groups_list.append(new_group)
    # print("Appended:%s" % old_groups_list)
    # print("%s\n%s" % (sorted(old_groups_list, key=Group.id_or_max), sorted(new_groups_list, key=Group.id_or_max)))
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)

