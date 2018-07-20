from model.group import Group


# совпадение списка групп в базе и на заглавной странице
def test_groups_list(app, db):
    ui_groups = app.group.get_groups_list()
    db_groups = db.get_groups_list()
    ui_groups_cleaned = [g.clean_group(id_transfer_to_int=True) for g in ui_groups]
    db_groups_cleaned = [g.clean_group(id_transfer_to_int=False) for g in db_groups]
    assert sorted(ui_groups_cleaned, key=Group.id_or_max) == sorted(db_groups_cleaned, key=Group.id_or_max)