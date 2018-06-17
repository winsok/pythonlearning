from model.group import Group

def test_editfirstgroup_name(app):
    old_groups = app.groups.get_group_list()
    app.groups.editfirstgroup(Group(name="New Name"))
    new_groups = app.groups.get_group_list()
    assert len(old_groups) == len(new_groups)



def test_editfirstgroup_header(app):
    old_groups = app.groups.get_group_list()
    app.groups.editfirstgroup(Group(header="New Header"))
    new_groups = app.groups.get_group_list()
    assert len(old_groups) == len(new_groups)