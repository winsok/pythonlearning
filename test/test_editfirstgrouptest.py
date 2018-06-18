from model.group import Group

def test_editfirstgroup_name(app):
    old_groups = app.groups.get_group_list()
    app.groups.editfirstgroup(Group(name="New Name"))
    assert len(old_groups) == app.groups.count()
    new_groups = app.groups.get_group_list()



def test_editfirstgroup_header(app):
    old_groups = app.groups.get_group_list()
    app.groups.editfirstgroup(Group(header="New Header"))
    assert len(old_groups) == app.groups.count()
    new_groups = app.groups.get_group_list()