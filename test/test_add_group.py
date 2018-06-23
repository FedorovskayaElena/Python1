# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups_list = app.group.get_groups_list()
    new_group = Group("Super Bowl 1", "New HHH", "New FFF")
    app.group.create(new_group)
    assert len(old_groups_list) + 1 == app.group.count()
    new_groups_list = app.group.get_groups_list()
    print("\n%s\n%s" % (old_groups_list, new_groups_list))
    old_groups_list.append(new_group)
    print("Appended:%s" % old_groups_list)
    print("%s\n%s" % (sorted(old_groups_list, key=Group.id_or_max), sorted(new_groups_list, key=Group.id_or_max)))
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)


def test_add_group_1(app):
    old_groups_list = app.group.get_groups_list()
    new_group = Group("Amar Hayam", "Хеадер 2", "Фуутер 2")
    app.group.create(new_group)
    assert len(old_groups_list) + 1 == app.group.count()
    new_groups_list = app.group.get_groups_list()
    print("\n%s\n%s" % (old_groups_list, new_groups_list))
    old_groups_list.append(new_group)
    print("Appended:%s" % old_groups_list)
    print("%s\n%s" % (sorted(old_groups_list, key=Group.id_or_max), sorted(new_groups_list, key=Group.id_or_max)))
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)

