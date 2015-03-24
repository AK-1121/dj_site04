#import selenium
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith open home page of online to-do app:
        self.browser.get('http://localhost:8000')

        # Title of the page:
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # Edith is invited to enter a to-do item strailght away

        # She types "Buy bananas" into a text box

        # When she hits enter, the page updates, and now the page lists:
        # "1: Buy bananas" as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # She enters "Make pie with bananas"

        # The page updates again, and now shows both items in her list

        # The site has generated a unique URL for her

        # She visits that URL - her to-do list is still there.


if __name__ == '__main__':
    unittest.main(warnings = 'ignore')


