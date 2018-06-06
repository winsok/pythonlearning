# -*- coding: utf-8 -*-
from model.group import Group

def test_addgrouptest(app):
    app.groups.create_group(Group(name="dadad", header="adada", footer="adda"))


def test2_addgrouptest(app):
    app.groups.create_group(Group(name="Lol", header="chto", footer="qwerty"))


