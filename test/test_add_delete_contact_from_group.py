# -*- coding: utf-8 -*-

from random import choice


# добавление контакта в группу
# если групп нет - группа добавляется из data/groups.json
# если нет контакта - контакт добавляется из data/contacts.json
def test_orm_add_contact_to_group_json(app, orm, one_random_json_contacts, one_random_json_groups):
    # получаем список групп
    group_list = orm.get_group_list_with_non_empty_names()
    # проверяем, если он пустой, создаем группу и перегружаем список
    if not len(group_list):
        app.group.create(one_random_json_groups)
        group_list = orm.get_group_list_with_non_empty_names()
        print("\nGroup created:%s" % group_list)
    # проверяем, есть ли контакты, если нет, создаем контакт без группы
    contact_list = orm.get_contact_list()
    if not len(contact_list):
        app.contact.create(one_random_json_contacts)
        contact_list = orm.get_contact_list()
        print("\nContact created:%s" % contact_list)
    # выбираем контакт и группу
    contact = choice(contact_list)
    group = choice(group_list)
    # считываем список контактов из нее
    contacts_in_group = orm.get_contacts_in_group(group)
    # если контакт уже в группе - удаляем контакт из группы
    if contact in contacts_in_group:
        app.contact.delete_contact_from_group(contact, group)
        contacts_in_group = orm.get_contacts_in_group(group)
    # присоединяем
    app.contact.link_contact_to_group(contact, group)
    print("\nContact %s added to %s" % (contact, group))
    # заново считываем список контактов из нее
    new_contacts_in_group = orm.get_contacts_in_group(group)
    # добавляем в исходную группу контакт
    contacts_in_group.append(contact)
    # проверяем, что списки равны
    assert contacts_in_group == new_contacts_in_group


# удаление контакта из группы
# если групп нет - группа добавляется из data/groups.json
# если нет контакта - контакт добавляется из data/contacts.json
def test_orm_delete_contact_from_group_json(app, orm, one_random_json_contacts, one_random_json_groups):

    # ищем группы с контактами или создаем такую
    # получаем список групп
    group_list = orm.get_group_list_with_non_empty_names()
    # проверяем, если он пустой, создаем группу и перегружаем список
    if not len(group_list):
        app.group.create(one_random_json_groups)
        group_list = orm.get_group_list_with_non_empty_names()
        print("\nGroup created:%s" % group_list)

    # проверяем, есть ли контакты, если нет, создаем контакт в случайной группе
    contact_list = orm.get_contact_list()
    if not len(contact_list):
        app.contact.create_contact_in_group(one_random_json_contacts, choice(group_list))
        contact_list = orm.get_contact_list()
        print("\nContact created:%s" % contact_list)
    # проверяем, есть ли группы с контактами, если нет, привязываем контакт к имеющейся группе
    else:
        groups_with_contacts = orm.get_groups_with_contacts_and_non_empty_names()
        if not len(groups_with_contacts):
            # создаем контакт через интерфейс без участия пони
            contact = choice(contact_list)
            group = choice(group_list)
            app.contact.link_contact_to_group(contact, group)
            print("\nContact %s added to %s" % (contact, group))

    groups_with_contacts = orm.get_groups_with_contacts_and_non_empty_names()

    group = choice(groups_with_contacts)
    contacts_in_group = orm.get_contacts_in_group(group)
    contact = choice(contacts_in_group)

    # удаляем контакт из группы
    app.contact.delete_contact_from_group(contact, group)
    # считываем новый список контактов в группе
    new_contacts_in_group = orm.get_contacts_in_group(group)
    # тестовая печать всего на свете
    print("\nСтарый список:%s" % contacts_in_group)
    print("\nНовый список:%s" % new_contacts_in_group)
    # убираем удаленную группу из исходного списка
    contacts_in_group.remove(contact)
    # проверяем, что списки равны
    assert contacts_in_group == new_contacts_in_group

