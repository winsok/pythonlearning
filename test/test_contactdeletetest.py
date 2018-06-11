from model.contact import Contact

def test_contactstest(app):
    if app.contacts.contacts_count() == 0:
        app.contacts.create_new_contact(Contact(firstname="crab"))
    app.contacts.delete_last_contact()


