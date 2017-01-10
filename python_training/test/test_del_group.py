from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="None"))
    old_groups_list = app.group.get_groups_list()
    app.group.delete_first()
    new_groups_list = app.group.get_groups_list()
    assert len(old_groups_list) - 1 == len(new_groups_list)
    old_groups_list[0:1] = []
    assert old_groups_list == new_groups_list


