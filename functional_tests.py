from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase) :

    def setUp(self) :
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self) :
        self.browser.quit()

    def test_can_start_a_list_and_retreive_it_later(self) :
        # Edith opens the TO-DO app
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # She enters a To-Do - "Buy peacock feathers".
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        # She sees the To-Do
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows), "New to-do item did not appear in table")
        # She can enter another To-Do - "Use peacock feathers to make a fly"
        self.fail('Finish the test!')
        # She sees the 2 To-Do's

        # The site generates a unique URL

        # She visits the URL, her list is still there

        # She goed to sleep

if __name__ == '__main__' :
    unittest.main(warnings = 'ignore')
