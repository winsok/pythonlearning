from model.group import Group
import random

def test_edit_some_firstgroup_name(app,db):
    if app.groups.count() == 0:
        app.groups.create(Group(name ="test"))
    old_groups = db.get_grouplist()
    group = random.choice(old_groups)
    group_data = Group(name="New Name")
    app.groups.edit_group_by_id(group.id, group_data)
    new_groups = db.get_grouplist()
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



#def test_editfirstgroup_header(app):
#    if app.groups.count() == 0:
#        app.groups.create(Group(name ="test"))
#    old_groups = app.groups.get_group_list()
#    app.groups.editfirstgroup(Group(header="New Header"))
#    assert len(old_groups) == app.groups.count()
#    new_groups = app.groups.get_group_list()