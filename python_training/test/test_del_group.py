from model.group import Group
from random import randrange


def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="None"))
    old_groups_list = app.group.get_groups_list()
    index = randrange(len(old_groups_list))
    app.group.delete_group_by_index(index)
    assert len(old_groups_list) - 1 == app.group.count()
    new_groups_list = app.group.get_groups_list()
    old_groups_list[index:index+1] = []
    assert old_groups_list == new_groups_list


