import re
from random import randint

def test_emails_on_home_page(app):
    contacts_count = app.contacts.count()
    random_contact = randint(0, contacts_count) - 1
    contact_from_home_page = app.contacts.get_contact_list()[random_contact]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(random_contact)
    assert contact_from_home_page.all_emails_on_homepage == merge_emails_like_on_home_page(contact_from_edit_page)

def test_phones_on_home_page(app):
    contacts_count = app.contacts.count()
    random_contact = randint(0, contacts_count) - 1
    contact_from_home_page = app.contacts.get_contact_list()[random_contact]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(random_contact)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_firstname_on_home_page(app):
    contacts_count = app.contacts.count()
    random_contact = randint(0, contacts_count) - 1
    contact_from_home_page = app.contacts.get_contact_list()[random_contact]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(random_contact)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname

def test_lastname_on_home_page(app):
    contacts_count = app.contacts.count()
    random_contact = randint(0, contacts_count) - 1
    contact_from_home_page = app.contacts.get_contact_list()[random_contact]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(random_contact)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname

def test_address_on_home_page(app):
    contacts_count = app.contacts.count()
    random_contact = randint(0, contacts_count) - 1
    contact_from_home_page = app.contacts.get_contact_list()[random_contact]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(random_contact)
    assert contact_from_home_page.address == contact_from_edit_page.address

def test_phones_on_contact_view_page(app):
    contacts_count = app.contacts.count()
    random_contact = randint(0, contacts_count) - 1
    contact_from_view_page = app.contacts.get_contact_from_view_page(random_contact)
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(random_contact)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                                      [contact.home, contact.mobile,contact.work,contact.phone2]))))
def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                                      [contact.email, contact.email2, contact.email3]))))




