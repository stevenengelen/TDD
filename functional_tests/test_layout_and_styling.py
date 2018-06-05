from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class LayoutAndStylingTest(FunctionalTest) :

    def test_layout_and_styling(self) :
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        # using i3, so calculating a terminal next to a browser window in the test below
        # self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.get_item_input_box()
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

        inputbox = self.get_item_input_box()
        # using i3, so calculating a terminal next to a browser window in the test below
        self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] / 2,
                480,
                delta = 5
                )
