from model.contact import Contact


def test_editfirstcontact_firstname(app):
    old_contacts = app.contacts.get_contact_list()
    app.contacts.edit_first_contact(Contact(firstname="New FirstName"))
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_editfirstcontact_middlename(app):
    old_contacts = app.contacts.get_contact_list()
    app.contacts.edit_first_contact(Contact(middlename="New MiddleName"))
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) == len(new_contacts)