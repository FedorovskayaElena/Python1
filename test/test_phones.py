import random
from model.technical import clear_extra_spaces
from model.technical import clear_phones


# проверка для случайно выбранного контакта
# совпадения телефонов на главной странице и на странице редактирования
def test_phones_on_home_page(app):
    index = random.randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    # склейка телефонов, полученных со страницы редактирования
    all_phones_from_edit_page = contact_from_edit_page.merge_cleaned_phones_like_on_home()
    # тестовая печать
    print("\nEdit page: %s" % clear_phones(all_phones_from_edit_page))
    print("\nHome page: %s" % clear_phones(contact_from_home_page.all_phones_from_homepage))
    # проверяем вначале, тот ли это контакт
    assert contact_from_home_page.contact_id == contact_from_edit_page.contact_id
    # проверка телефонов
    assert clear_phones(contact_from_home_page.all_phones_from_homepage) == clear_phones(all_phones_from_edit_page)


# проверка для случайно выбранного контакта
# совпадения телефонов на странице просмотра и на странице редактирования
def test_phones_on_view_page(app):
    index = random.randrange(app.contact.count())
    contact_from_view_page = app.contact.get_all_content_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    all_phones_from_edit_page = merge_phones_from_edit_like_on_viewpage(contact_from_edit_page)
    secondary_phone_from_edit = secondary_phone_from_edit_like_on_viewpage(contact_from_edit_page)

    # тестовая печать
    print("\nEdit page: %s" % all_phones_from_edit_page)
    print("\nEdit page: %s" % secondary_phone_from_edit)

    print("\nView page:\n %s" % contact_from_view_page.all_content_from_viewpage)

    print("\nSearch Res 1:\n %s" % contact_from_view_page.all_content_from_viewpage.find(all_phones_from_edit_page))
    print("\nSearch Res 2:\n %s" % contact_from_view_page.all_content_from_viewpage.find(secondary_phone_from_edit))

    assert contact_from_view_page.contact_id == contact_from_edit_page.contact_id
    assert contact_from_view_page.all_content_from_viewpage.find(all_phones_from_edit_page) >= 0 and \
           contact_from_view_page.all_content_from_viewpage.find(secondary_phone_from_edit) >= 0


# склеивание телефонов со страницы редакторования в единый блок, как на странице просмотра (без секондари телефона)
def merge_phones_from_edit_like_on_viewpage(contact):
    prefixes = ["H: ", "M: ", "W: "]
    phones = [contact.homephone, contact.mobilephone, contact.workphone]
    merged_phones = ""
    for i in range(0, len(phones)):
        if phones[i] != '':
            merged_phones = merged_phones + ("\n%s%s" % (str(prefixes[i]), clear_extra_spaces(phones[i])))
    # print("Merged phones: \n" + str(merged_phones))
    return merged_phones


# форматирование секондари-телефона со страницы редактирования так,
# чтобы можно было сравнить со страницей просмотра для уменьшения
# вероятности ложного срабатывания на P:
def secondary_phone_from_edit_like_on_viewpage(contact):
    if contact.phone2 is '':
        return contact.phone2
    else:
        return "P: " + clear_extra_spaces(contact.phone2)


