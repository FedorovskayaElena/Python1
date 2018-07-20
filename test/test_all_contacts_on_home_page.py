

# сверка всех контактов на главной странице с базой данных
# по полям - имя, фамилия, адрес, телефоны, адреса электронной почты

def test_all_contacts_on_home_page(app, db):
    contacts_from_home_page = sorted(app.contact.get_contacts_list(), key=lambda c: c.id_or_max())
    contacts_from_db = db.get_contacts_list()
    # одинаковое ли количество контактов в базе и на главной странице
    assert len(contacts_from_home_page) == len(contacts_from_db)
    # проверка по каждому контакту
    for i in range(0, len(contacts_from_db)):
        # склейка телефонов и емейлов, полученных из базы как на заглавной странице
        cleaned_phones_like_on_home = contacts_from_db[i].merge_cleaned_phones_like_on_home()
        cleaned_emails_like_on_home = contacts_from_db[i].merge_cleaned_emails_like_on_home()

        print("\nDB phones:\n_%s_" % cleaned_phones_like_on_home)
        print("\nHome page phones:\n_%s_" % contacts_from_home_page[i].all_phones_from_homepage)
        print("\nDB emails:\n_%s_" % cleaned_emails_like_on_home)
        print("\nHome page emails:\n_%s_" % contacts_from_home_page[i].all_emails_from_homepage)

        # проверки - вначале стандартная, совпадение id, lastname, firstname, address
        assert contacts_from_home_page[i] == contacts_from_db[i]

        # потом отдельно склеенные как на заглавной телефоны и емейлы
        assert cleaned_phones_like_on_home == contacts_from_home_page[i].all_phones_from_homepage
        assert cleaned_emails_like_on_home == contacts_from_home_page[i].all_emails_from_homepage




