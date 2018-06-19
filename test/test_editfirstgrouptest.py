from model.group import Group
from random import randrange

def test_edit_some_firstgroup_name(app):
    if app.groups.count() == 0:
        app.groups.create(Group(name ="test"))
    old_groups = app.groups.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New Name")
    group.id = old_groups[index].id
    app.groups.edit_group_by_index(index, group)
    new_groups = app.groups.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



#def test_editfirstgroup_header(app):
#    if app.groups.count() == 0:
#        app.groups.create(Group(name ="test"))
#    old_groups = app.groups.get_group_list()
#    app.groups.editfirstgroup(Group(header="New Header"))
#    assert len(old_groups) == app.groups.count()
#    new_groups = app.groups.get_group_list()