from selenium import webdriver
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
        self.fail('Finish the test!')

        # She enters a To-Do - "Buy peacock feathers".

        # She sees the To-Do

        # She can enter another To-Do - "Use peacock feathers to make a fly"

        # She sees the 2 To-Do's

        # The site generates a unique URL

        # She visits the URL, her list is still there

        # She goed to sleep

if __name__ == '__main__' :
    unittest.main(warnings = 'ignore')
