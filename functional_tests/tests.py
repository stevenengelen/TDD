from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from contextlib import contextmanager
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.ui import WebDriverWait
import sys

class NewVisitorTest(StaticLiveServerTestCase) :

    def setUp(self) :
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self) :
        self.browser.quit()

    @classmethod
    def setUpClass(cls) :
        for arg in sys.argv :
            if 'liveserver' in arg :
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls) :
        if cls.server_url == cls.live_server_url :
            super().tearDownClass()
        
    @contextmanager
    def wait_for_page_load(self, timeout = 50) :
        old_page = self.browser.find_element_by_tag_name('html')
        yield
        WebDriverWait(self.browser, timeout).until(staleness_of(old_page))

    def check_for_row_in_list_table(self, row_text) :
        '''
        start_time = time.time()
        while time.time() < start_time + 10 :
            try :
                table = self.browser.find_element_by_id('id_list_table')
            except StaleElementReferenceException :
                time.sleep(0.1)
        '''
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self) :
        # Edith opens the TO-DO app
        self.browser.get(self.server_url)

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        # She enters a To-Do - "Buy peacock feathers".
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(5)

        # She gets redirected to her URL, sees her list and her item.
        # with self.wait_for_page_load() :
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # She enters another To-Do - "Use peacock feathers to make a fly".
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(5)
        
        # She sees the 2 To-Do's.
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Francis comes along
        # Francis launches a new browser sesion (to make sure there are no cookies left).
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # Francis does not see Edith's list in the browser.
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
        
        # Francis enters a new item and thus starts a new list.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis gets his URL
        # with self.wait_for_page_load() :
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # There is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # self.fail('Finish the test!')

        # The site generates a unique URL

        # She visits the URL, her list is still there

        # She goes to sleep

    def test_layout_and_styling(self) :
        # Edith goes to the home page
        self.browser.get(self.server_url)
        # using i3, so calculating a terminal next to a browser window in the test below
        # self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        # using i3, so calculating a terminal next to a browser window in the test below
        self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] / 2,
                480,
                delta = 5
                )

        # She starts a new list and sees the input is nicely centered here too
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        
        # with self.wait_for_page_load() :
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        
        inputbox = self.browser.find_element_by_id('id_new_item')
        # using i3, so calculating a terminal next to a browser window in the test below
        self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] / 2,
                480,
                delta = 5
                )
