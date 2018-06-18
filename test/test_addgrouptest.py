# -*- coding: utf-8 -*-
from model.group import Group

def test_addgrouptest(app):
    old_groups = app.groups.get_group_list()
    group = Group(name="dadad", header="adada", footer="adda")
    app.groups.create_group(group)
    assert len(old_groups) + 1 == app.groups.count()
    new_groups = app.groups.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test2_addgrouptest(app):
    old_groups = app.groups.get_group_list()
    group = Group(name="Lol", header="chto", footer="qwerty")
    app.groups.create_group(group)
    assert len(old_groups) + 1 == app.groups.count()
    new_groups = app.groups.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

