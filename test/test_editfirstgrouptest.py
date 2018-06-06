from model.group import Group

def test_editfirstgroup_name(app):
    app.groups.editfirstgroup(Group(name="New Name"))



def test_editfirstgroup_header(app):
    app.groups.editfirstgroup(Group(header="New Header"))