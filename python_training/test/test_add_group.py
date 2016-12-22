# -*- coding: utf-8 -*-

import pytest
from model.group import Group


def test_add_group(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="hoho", header="vjl", footer="bho"))
        app.session.logout()


def test_add_empty_group(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="", header="", footer=""))
        app.session.logout()
