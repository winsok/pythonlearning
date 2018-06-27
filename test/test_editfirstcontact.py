from model.contact import Contact
from random import randrange


def test_edit_some_contact_firstname(app):
    if app.contacts.count() == 0:
        app.contacts.create_new_contact(Contact(firstname="crab",home="23131", work="23131313", mobile="23131", phone2="213131313"))
    old_contacts = app.contacts.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New FirstName")
    contact.id = old_contacts[index].id
    app.contacts.edit_contact_by_index(index, contact)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



#def test_editfirstcontact_middlename(app):
#    if app.contacts.count() == 0:
#        app.contacts.create_new_contact(Contact(firstname="crab"))
#    old_contacts = app.contacts.get_contact_list()
#    app.contacts.edit_first_contact(Contact(middlename="New MiddleName"))
#    new_contacts = app.contacts.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)