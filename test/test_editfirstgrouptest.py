from model.group import Group

def test_editfirstgroup_name(app):
    app.session.login(username="admin", password="secret")
    app.groups.editfirstgroup(Group(name="New Name"))
    app.session.logout()


def test_editfirstgroup_header(app):
    app.session.login(username="admin", password="secret")
    app.groups.editfirstgroup(Group(header="New Header"))
    app.session.logout()