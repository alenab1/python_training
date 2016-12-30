from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="None"))
    app.group.edit_first(Group(name="hohoxxx", header="vjlyyy", footer="bhozzz"))


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="None"))
    app.group.edit_first(Group(name="New group"))


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="None"))
    app.group.edit_first(Group(header="New header"))
