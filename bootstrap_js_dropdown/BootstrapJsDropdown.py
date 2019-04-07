from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class DropDownMenu(object):
    drop_down_toggle_locator = (By.CLASS_NAME, "dropdown-toggle")
    drop_down_selector = (By.CLASS_NAME, "dropdown")
    drop_down_menu_locator = (By.CLASS_NAME, "dropdown-menu")

    def __init__(self, dropdown):
        if 'dropdown' not in dropdown.get_attribute('class'):
            raise NoSuchElementException("Wrong element")

        self.dropdown_container = dropdown
        self.drop_down_menu = self.dropdown_container.find_element(*self.drop_down_menu_locator)
        self.dropdown_toggle = self.dropdown_container.find_element(*self.drop_down_toggle_locator)

    @property
    def options(self):
        self.open_menu()
        return self.drop_down_menu.find_elements(By.TAG_NAME, "li")

    @property
    def selected_option(self):
        return self.dropdown_toggle.text

    def select_value_by_index(self, index=0):
        self.options[index].click()

    def select_value_by_name(self, name):
        [i for i in self.options if i.text.strip() == name][0].click()

    def select_value_by_partial_name(self, name):
        [i for i in self.options if i.text in name][0].click()

    def select_value_by_class_name(self, class_name):
        [i for i in self.options if class_name in i.get_attribute('class')][0].click()

    def open_menu(self):
        if self.is_menu_open() is False:
            self.dropdown_toggle.click()

    def is_menu_open(self):
        return 'open' in self.dropdown_container.get_attribute('class')
