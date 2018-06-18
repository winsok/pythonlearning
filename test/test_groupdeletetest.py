from model.group import Group

def test_delete_first_group(app):
    if app.groups.count() == 0:
        app.groups.create(Group(name ="test"))
    old_groups = app.groups.get_group_list()
    app.groups.delete_first()
    assert len(old_groups) - 1 == app.groups.count()
    new_groups = app.groups.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups