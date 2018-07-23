# -*- coding: utf-8 -*-

from model.contact import Contact


def test_contactstest(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contacts.create_new_contact(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


