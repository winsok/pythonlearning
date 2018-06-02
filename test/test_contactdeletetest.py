
def test_contactstest(app):
    app.session.login(username="admin", password="secret")
    app.contacts.delete_last_contact()
    app.session.logout()