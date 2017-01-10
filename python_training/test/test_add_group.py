# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
        old_groups_list = app.group.get_groups_list()
        group = Group(name="hoho", header="vjl", footer="bho")
        app.group.create(group)
        new_groups_list = app.group.get_groups_list()
        assert len(old_groups_list) + 1 == len(new_groups_list)
        old_groups_list.append(group)
        assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)


def test_add_empty_group(app):
        old_groups_list = app.group.get_groups_list()
        group = Group(name="", header="", footer="")
        app.group.create(group)
        new_groups_list = app.group.get_groups_list()
        assert len(old_groups_list) + 1 == len(new_groups_list)
        old_groups_list.append(group)

        assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)

