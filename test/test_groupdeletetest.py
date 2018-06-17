from model.group import Group

def test_delete_first_group(app):
    if app.groups.count() == 0:
        app.groups.create(Group(name ="test"))
    old_groups = app.groups.get_group_list()
    app.groups.delete_first()
    new_groups = app.groups.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)