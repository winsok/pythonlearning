

def test_editfirstgroup(app):
    app.session.login(username="admin", password="secret")
    app.groups.editfirstgroup()
    app.session.logout()


