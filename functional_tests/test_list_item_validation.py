from .base import FunctionalTest
from unittest import skip
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest) :

    def test_cannot_add_empty_list_items(self) :
        # Edith goes to the home page and accidentaly tries to submit an empty list item.
        # She hits Enter on the empty input box
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # The home page refreshes, and there is an error message saying that list items
        # cannot be blank
        # The browser intercepts the request, and does not load the list page
        # self.wait_for(lambda : self.browser.find_element_by_css_selector('.has-error'))
        # self.browser.find_element_by_css_selector('.has-error'))
        self.browser.find_element_by_css_selector('#id_text:invalid')
        # self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with some text for the item, which now works
        self.get_item_input_box().send_keys('Buy milk\n')
        self.browser.find_element_by_css_selector('#id_text:invalid')
        self.get_item_input_box().send_keys('\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # Peversely, she now decides to submit a second blank list item
        self.get_item_input_box().send_keys('\n')

        # She receives a similar warning on the list page
        self.check_for_row_in_list_table('1: Buy milk')
        self.browser.find_element_by_css_selector('#id_text:invalid')

        # And she can correct it by filling some text in
        self.get_item_input_box().send_keys('Make tea\n')
        self.browser.find_element_by_css_selector('#id_text:invalid')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
