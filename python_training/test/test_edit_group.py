from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="None"))
    old_groups_list = app.group.get_groups_list()
    group = Group(name="hohoxxx", header="vjlyyy", footer="bhozzz")
    group.id = old_groups_list[0].id
    app.group.edit_first(group)
    new_groups_list = app.group.get_groups_list()
    assert len(old_groups_list) == len(new_groups_list)
    old_groups_list[0] = group
    assert sorted(old_groups_list, key=app.id_or_max) == sorted(new_groups_list, key=app.id_or_max)


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="None"))
    old_groups_list = app.group.get_groups_list()
    group = Group(name="New group")
    group.id = old_groups_list[0].id
    app.group.edit_first(group)
    new_groups_list = app.group.get_groups_list()
    assert len(old_groups_list) == len(new_groups_list)
    old_groups_list[0] = group
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)

#
# def test_edit_first_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="None"))
#     old_groups_list = app.group.get_groups_list()
#     group = Group(header="New header")
#     group.id = old_groups_list[0].id
#     app.group.edit_first(group)
#     new_groups_list = app.group.get_groups_list()
#     assert len(old_groups_list) == len(new_groups_list)
#     old_groups_list[0] = group
#     assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)
