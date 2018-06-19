from model.contact import Contact

def test_contactstest(app):
    if app.contacts.count() == 0:
        app.contacts.create_new_contact(Contact(firstname="crab"))
    old_contacts = app.contacts.get_contact_list()
    app.contacts.delete_last_contact()
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


