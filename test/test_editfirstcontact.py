from model.contact import Contact
import random


def test_edit_some_contact_firstname(app, db, check_ui):
    if app.contacts.count() == 0:
        app.contacts.create_new_contact(Contact(firstname="crab"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_data = Contact(firstname="helloman")
    contact_data.id = contact.id
    app.contacts.edit_contact_by_id(contact.id, contact_data)
    old_contacts.remove(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact_data)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)



#def test_editfirstcontact_middlename(app):
#    if app.contacts.count() == 0:
#        app.contacts.create_new_contact(Contact(firstname="crab"))
#    old_contacts = app.contacts.get_contact_list()
#    app.contacts.edit_first_contact(Contact(middlename="New MiddleName"))
#    new_contacts = app.contacts.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)