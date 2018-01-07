from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys

class FunctionalTest(StaticLiveServerTestCase) :
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

    '''
    @classmethod
    def tearDownClass(cls) :
        print(cls.server_url)
        if cls.server_url == cls.live_server_url :
            super().tearDownClass()
    '''
    '''
    @contextmanager
    def wait_for_page_load(self, timeout = 50) :
        old_page = self.browser.find_element_by_tag_name('html')
        yield
        WebDriverWait(self.browser, timeout).until(staleness_of(old_page))
    '''
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
