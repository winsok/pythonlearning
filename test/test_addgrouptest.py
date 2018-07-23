# -*- coding: utf-8 -*-
from model.group import Group


def test_addgrouptest(app, db, json_groups):
    group = json_groups
    old_groups = db.get_grouplist()
    app.groups.create_group(group)
    new_groups = db.get_grouplist()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




