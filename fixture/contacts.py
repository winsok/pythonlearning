

class ContactsHelper:

    def __init__(self, app):
        self.app = app

    def create_new_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_data(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_homepage()

    def fill_contact_data(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("byyear", contact.byear)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_last_contact(self):
        wd = self.app.wd
        self.app.open_homepage()
        self.select_first_contact()
        wd.find_element_by_css_selector("input[value=Delete]").click()
        wd.switch_to_alert().accept()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_homepage()
        self.select_first_contact()
        # edit
        wd.find_element_by_css_selector("img[title=Edit]").click()
        # fill in contact form
        self.fill_contact_data(new_contact_data)
        # submit changes
        wd.find_element_by_name("update").click()
        self.app.open_homepage()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()




