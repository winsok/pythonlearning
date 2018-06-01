# -*- coding: utf-8 -*-
from application import Application
from group import Group
import pytest

@pytest.fixture
def app(request):
    fixture: Application = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_addgrouptest(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="dadad", header="adada", footer="adda"))
    app.logout()

def test2_addgrouptest(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Lol", header="chto", footer="qwerty"))
    app.logout()

