# -*- coding: utf-8 -*-
from model.group import Group
from random import choice
import pytest


test_data = [i for i in range(2)]


@pytest.mark.parametrize("number", test_data)
def test_modify_group(app, db, number, check_ui):
    if app.group.count() == 0:
        app.group.create(Group("Added from test_modify", "Header 2", "Footer 2"))
    old_groups_list = db.get_groups_list()
    modify_group = choice(old_groups_list)
    print("Random index: %s" % str(modify_group.group_id))
    new_group = Group(name="Четверговая %s" % str(number), group_id=modify_group.group_id)
    app.group.modify_by_id(new_group, modify_group.group_id)

    new_groups_list = db.get_groups_list()
    # удаляем и заменяем на новую
    modify_index = old_groups_list.index(modify_group)
    old_groups_list[modify_index].name = new_group.name

    assert sorted(old_groups_list, key=lambda g: g.group_id) == new_groups_list

    # а вот список из интерфейса надо сортировать
    # # и раз в интерфейсе пробелмы чистятся, то лучше и наши оба списка от пробелов почистить
    if check_ui:
        new_groups_list_cleaned = [g.clean_group() for g in new_groups_list]
        ui_groups_list_cleaned = [g.clean_group() for g in app.group.get_groups_list()]
        assert new_groups_list_cleaned == sorted(ui_groups_list_cleaned, key=lambda gr: gr.id_or_max())
        print("Checked UI")

