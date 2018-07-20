# -*- coding: utf-8 -*-
from model.group import Group
from random import choice
import pytest


test_data = [i for i in range(5)]


@pytest.mark.parametrize("number", test_data)
def test_delete_group(app, db, number, check_ui):
    if app.group.count() == 0:
        app.group.create(Group("Added from test_delete", "Header 2", "Footer 2"))
    old_groups_list = db.get_groups_list()
    delete_group = choice(old_groups_list)
    app.group.delete_by_id(delete_group.group_id)
    print("Random id: %s" % str(delete_group.group_id))
    new_groups_list = db.get_groups_list()
    print("Old:\n%s\nNew:\n%s" % (old_groups_list, new_groups_list))
    old_groups_list.remove(delete_group)
    assert old_groups_list == new_groups_list
    if check_ui:
        assert new_groups_list == \
               sorted(app.group.get_groups_list(), key=lambda gr: gr.id_or_max())
        print("checked_ui")


