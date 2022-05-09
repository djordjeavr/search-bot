from selenium import webdriver
from time import sleep
import random


class SearchBot(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers\chromedriver.exe", base_url="https://www.google.com"):
        self.driver_path = driver_path
        self.base_url = base_url
        self.driver = webdriver.Chrome(executable_path=self.driver_path)

    def land_first_page(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def hand_typed_value(self, value, field):
        for i, v in enumerate(value):
            field.send_keys(v)
            sleep(random.random())

    def inserting_values(self, value):
        search_input = self.driver.find_element_by_class_name('gLFyf')
        self.hand_typed_value(value, search_input)
        search_button = self.driver.find_element_by_class_name('gNO89b')
        sleep(3)
        search_button.click()

    def open_website(self):
        parent_website_link = self.driver.find_element_by_class_name('yuRUbf')
        website_link = parent_website_link.find_element_by_css_selector('a')
        website_link.click()

    def accept_cookie(self):

        if (self.driver.driver.find_elements_by_css_selector('.cli-bar-btn_container')):
            parent_accept_button = self.driver.find_element_by_class_name('cli-bar-btn_container')
            accept_button = parent_accept_button.find_element_by_class_name('cli_action_button')
            accept_button.click()
