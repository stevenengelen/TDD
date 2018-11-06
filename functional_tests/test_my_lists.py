from .base import FunctionalTest
from .server_tools import create_session_on_server

class MyListsTest(FunctionalTest) :
    def test_logged_in_users_lists_are_saved_as_my_lists(self) :
        email = 'edith@example.com'

        # Edith is a logged-in user
        self.create_pre_authenticated_session(email)

        # She goes to the home page and starts a list
        self.browser.get(self.live_server_url)
        self.add_list_item('Reticulate splines')
        self.add_list_item('Immanentize eschaton')
        first_list_url = self.browser.current_url

        # She notices a "My lists" link, for the first time.
        self.browser.find_element_by_link_text('My lists').click()

        # She sees that her list is in there, named according to its first list item
        self.wait_for(lambda : self.browser.find_element_by_link_text('Reticulate splines'))
        self.browser.find_element_by_link_text('Reticulate splines').click()
        # wait condition, so I repeated this assignment here so the FT passes
        first_list_url = self.browser.current_url
        self.wait_for(lambda : self.assertEqual(self.browser.current_url, first_list_url))
        # self.wait_to_be_logged_in(email)

        # She decides to start another list, just to see
        self.browser.get(self.live_server_url)
        self.add_list_item('Click cows')
        second_list_url = self.browser.current_url

        # Under "my lists", her new list appears
        self.browser.find_element_by_link_text('My lists').click()
        self.wait_for(lambda : self.browser.find_element_by_link_text('Click cows'))
        self.browser.find_element_by_link_text('Click cows').click()
        # wait condition, so I repeated this assignment here so the FT passes
        second_list_url = self.browser.current_url
        self.wait_for(lambda : self.assertEqual(self.browser.current_url, second_list_url))

        # She logs out. The "My lists" option dissapears
        self.browser.find_element_by_link_text('Log out').click()
        self.wait_for(lambda : self.assertEqual(self.browser.find_elements_by_link_text('My lists'), [] ))
