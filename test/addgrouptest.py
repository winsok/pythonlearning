# -*- coding: utf-8 -*-
from model.group import Group

def test_addgrouptest(app):
    app.session.login(username="admin", password="secret")
    app.groups.create_group(Group(name="dadad", header="adada", footer="adda"))
    app.session.logout()

def test2_addgrouptest(app):
    app.session.login(username="admin", password="secret")
    app.groups.create_group(Group(name="Lol", header="chto", footer="qwerty"))
    app.session.logout()

