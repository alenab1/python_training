from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first(Group(name="hohoxxx", header="vjlyyy", footer="bhozzz"))


def test_edit_first_group_name(app):
    app.group.edit_first(Group(name="New group"))


def test_edit_first_group_header(app):
    app.group.edit_first(Group(header="New header"))
