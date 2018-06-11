from model.contact import Contact


def test_editfirstcontact_firstname(app):
    app.contacts.edit_first_contact(Contact(firstname="New FirstName"))

def test_editfirstcontact_middlename(app):
    app.contacts.edit_first_contact(Contact(middlename="New MiddleName"))