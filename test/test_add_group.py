# -*- coding: utf-8 -*-
from model.group import Group


# запуск тестовой функции на данных в файле JSON
def test_add_group_json(app, db, json_groups, check_ui):
    new_group = json_groups
    old_groups_list = db.get_groups_list()
    app.group.create(new_group)
    new_groups_list = db.get_groups_list()
    old_groups_list.append(new_group)
    # перед сравнением лишние пробелы не удаляем, т.к. группы не считываются из интерфейса, где обрезаются пробелы
    # сортируем только тот список, в который сами добавляли группу
    assert sorted(old_groups_list, key=Group.id_or_max) == new_groups_list
    # а вот список из интерфейса надо сортировать
    # и раз в интерфейсе пробелмы чистятся, то лучше и наши оба списка от пробелов почистить
    if check_ui:
        new_groups_list_cleaned = [g.clean_group() for g in new_groups_list]
        ui_groups_list_cleaned = [g.clean_group() for g in app.group.get_groups_list()]
        assert new_groups_list_cleaned == sorted(ui_groups_list_cleaned, key=lambda gr: gr.id_or_max())
        print("Checked UI")


# запуск тестовой функции на данных в файле питон
def test_add_group_module(app, db, data_groups, check_ui):
    new_group = data_groups
    old_groups_list = db.get_groups_list()
    app.group.create(new_group)
    new_groups_list = db.get_groups_list()
    old_groups_list.append(new_group)
    # перед сравнением лишние пробелы не удаляем, т.к. группы не считываются из интерфейса, где обрезаются пробелы
    # сортируем только тот список, в который сами добавляли группу
    assert sorted(old_groups_list, key=Group.id_or_max) == new_groups_list
    # а вот список из интерфейса надо сортировать
    # и раз в интерфейсе пробелмы чистятся, то лучше и наши оба списка от пробелов почистить
    if check_ui:
        new_groups_list_cleaned = [g.clean_group() for g in new_groups_list]
        ui_groups_list_cleaned = [g.clean_group() for g in app.group.get_groups_list()]
        assert new_groups_list_cleaned == sorted(ui_groups_list_cleaned, key=lambda gr: gr.id_or_max())
        print("Checked UI")
