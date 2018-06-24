import random


# проверка для случайно выбранного контакта
# совпадения информации на главной странице и на странице редактирования
# для полей - имя, фамилия, адрес, телефоны, адреса электронной почты
def test_contact_on_home_and_edit(app):
    index = random.randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    print("\n%s == %s" % (contact_from_home_page.firstname, contact_from_edit_page.firstname))
    print("\n%s == %s" % (contact_from_home_page.lastname, contact_from_edit_page.lastname))
    print("\n%s == %s" % (contact_from_home_page.address, contact_from_edit_page.address))
    # склейка телефонов, полученных со страницы редактирования
    all_phones_from_edit_page = app.contact.merge_phones_from_edit_like_on_home(contact_from_edit_page)
    # тестовая печать
    print("\nEdit page: %s" % app.contact.clear_phones(all_phones_from_edit_page))
    print("\nHome page: %s" % app.contact.clear_phones(contact_from_home_page.all_phones_from_homepage))
    # склейка emails, полученных со страницы редактирования
    all_emails_from_edit_page = merge_emails_from_edit_like_on_home(contact_from_edit_page)
    # тестовая печать
    print("\nEdit page: %s" % app.contact.clear_phones(all_emails_from_edit_page))
    print("\nHome page: %s" % app.contact.clear_phones(contact_from_home_page.all_emails_from_homepage))
    # проверки (вначале проверяем тот ли контакт)
    assert contact_from_home_page.contact_id == contact_from_edit_page.contact_id
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert app.contact.clear_phones(contact_from_home_page.all_phones_from_homepage) == \
           app.contact.clear_phones(all_phones_from_edit_page)
    assert contact_from_home_page.all_emails_from_homepage == all_emails_from_edit_page


# склеивание email-ов со странцы редактирования в единый блок, как на домашней странице
def merge_emails_from_edit_like_on_home(contact):
    merged_emails = "\n".join(filter(lambda x: x != "", [contact.email, contact.email2, contact.email3]))
    return merged_emails


