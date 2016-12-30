
class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        self.init_group_creation(wd)
        # fill group form
        self.fill_group_form(group)
        self.submit_group_creation(wd)
        self.return_to_groups_page()

    def submit_group_creation(self, wd):
        wd.find_element_by_name("submit").click()

    def init_group_creation(self, wd):
        wd.find_element_by_name("new").click()

    def fill_group_form(self, group):
        self.app.change_field_value("group_name", group.name)
        self.app.change_field_value("group_header", group.header)
        self.app.change_field_value("group_footer", group.footer)

    def delete_first(self):
        wd = self.app.wd
        self.open_groups_page()
        self.app.click_first_entry_in_list()
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_first(self, new_group):
        wd = self.app.wd
        self.open_groups_page()
        self.app.click_first_entry_in_list()
        self.open_modification_form()
        self.fill_group_form(new_group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def open_modification_form(self):
        wd = self.app.wd
        wd.find_element_by_name("edit").click()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))