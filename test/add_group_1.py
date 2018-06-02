# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

# Создание фикстуры
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login("admin", "secret")
    app.create_group(Group("Name", "Header 2", "Footer 2"))
    app.session.logout()
