# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contactstest(app):
    old_contacts = app.contacts.get_contact_list()
    contact = Contact(firstname="akdjaasd",lastname="wkdjad", home="23131", work="23131313", mobile="23131", phone2="213131313")
    app.contacts.create_new_contact(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


