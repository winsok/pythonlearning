# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver 
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class addgrouptest(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_addgrouptest(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, name="dadad", header="adada", footer="adda")
        self.open_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd, name, header, footer):
        # open group page
        wd.find_element_by_link_text("groups").click()
        # start group creation
        wd.find_element_by_name("new").click()
        # fill in group data
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_homepage(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def test2_addgrouptest(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, name="Lol", header="chto", footer="qwerty")
        self.open_groups_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
