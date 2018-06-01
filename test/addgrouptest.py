# -*- coding: utf-8 -*-
from fixture.application import Application
from model.group import Group
import pytest

@pytest.fixture
def app(request):
    fixture: Application = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_addgrouptest(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="dadad", header="adada", footer="adda"))
    app.session.logout()

def test2_addgrouptest(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="Lol", header="chto", footer="qwerty"))
    app.session.logout()

