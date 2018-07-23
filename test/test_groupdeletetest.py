from model.group import Group
import random

def test_delete_some_group(app, db, check_ui):
    if len(db.get_grouplist()) == 0:
        app.groups.create(Group(name="test"))
    old_groups = db.get_grouplist()
    group = random.choice(old_groups)
    app.groups.delete_group_by_id(group.id)
    new_groups = db.get_grouplist()
    assert len(old_groups) - 1 == app.groups.count()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.groups.get_group_list(), key=Group.id_or_max)