from selenium import webdriver
from fixture.session import SessionHelper
from fixture.groups import GroupsHelper
from fixture.contacts import ContactsHelper

class Application:

    def __init__(self, browser="firefox"):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "Safari":
            self.wd = webdriver.Safari()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.groups = GroupsHelper(self)
        self.contacts = ContactsHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return  True
        except:
            return False

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()


