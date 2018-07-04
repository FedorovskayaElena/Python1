# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import pytest


test_data = [i for i in range(8)]


@pytest.mark.parametrize("number", test_data)
def test_delete_group(app, number):
    if app.group.count() == 0:
        app.group.create(Group("Added from test_delete", "Header 2", "Footer 2"))
    old_groups_list = app.group.get_groups_list()
    delete_index = randrange(len(old_groups_list))
    app.group.delete_by_index(delete_index)
    # print("Random index 1: %s" % str(delete_index))
    assert len(old_groups_list) - 1 == app.group.count()
    new_groups_list = app.group.get_groups_list()
    print("\n%s\n%s" % (old_groups_list, new_groups_list))
    old_groups_list[delete_index:delete_index+1] = []
    # print("Deleted:\n%s" % old_groups_list)
    # print("Sorted:\n%s\n%s" % (sorted(old_groups_list, key=lambda gr: gr.group_id),
    #                            sorted(new_groups_list, key=lambda gr: gr.group_id)))
    assert sorted(old_groups_list,  key=lambda gr: gr.group_id) == sorted(new_groups_list,  key=lambda gr: gr.group_id)

