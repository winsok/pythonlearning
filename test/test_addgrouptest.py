# -*- coding: utf-8 -*-
from model.group import Group

def test_addgrouptest(app):
    old_groups = app.groups.get_group_list()
    app.groups.create_group(Group(name="dadad", header="adada", footer="adda"))
    new_groups = app.groups.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test2_addgrouptest(app):
    old_groups = app.groups.get_group_list()
    app.groups.create_group(Group(name="Lol", header="chto", footer="qwerty"))
    new_groups = app.groups.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

