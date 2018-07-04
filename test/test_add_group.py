# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(postfix, maxlen):
    s = "".join([random.choice(string.ascii_letters + string.digits + " "*6) for i in range(random.randrange(maxlen))])
    return s + postfix


test_data = [Group(name="Группа в полосатых купальниках", header="Хедер группы в полосатых купальниках",
                   footer="Футер группы в полосатых купальниках")] + \
            [Group(name=name, header=header, footer=footer)
             for name in ["", random_string("name", 20)]
             for header in ["", random_string("header", 20)]
             for footer in ["", random_string("footer", 20)]] + \
            [Group(name=random_string("name", 20), header=random_string("header", 20), footer=random_string("footer", 20))
             for i in range(0, 5)]


@pytest.mark.parametrize("new_group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, new_group):
    old_groups_list = app.group.get_groups_list()
    app.group.create(new_group)
    assert len(old_groups_list) + 1 == app.group.count()
    new_groups_list = app.group.get_groups_list()
    # print("\n%s\n%s" % (old_groups_list, new_groups_list))
    old_groups_list.append(new_group)
    # print("Appended:%s" % old_groups_list)
    # print("%s\n%s" % (sorted(old_groups_list, key=Group.id_or_max), sorted(new_groups_list, key=Group.id_or_max)))
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)
