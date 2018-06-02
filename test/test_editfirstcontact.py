

def test_editfirstcontact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.edit_first_contact()
    app.session.logout()