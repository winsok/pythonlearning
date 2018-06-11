from model.group import Group

def test_delete_first_group(app):
    if app.groups.count() == 0:
        app.groups.create(Group(name ="test"))
    app.groups.delete_first()
