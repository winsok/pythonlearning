# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contactstest(app):
    old_contacts = app.contacts.get_contact_list()
    contact = Contact(firstname="akdjaasd",middlename="wkdjad")
    app.contacts.create_new_contact(contact)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


