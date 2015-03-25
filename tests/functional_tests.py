#import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        #self.browser = webdriver.Firefox()
        self.browser = webdriver.Chrome()
        #self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith open home page of online to-do app:
        self.browser.get('http://localhost:8000')
        #browser.get("http://stackoverflow.com")

        # Title of the page:
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Edith is invited to enter a to-do item strailght away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # She types "Buy bananas" into a text box
        inputbox.send_keys('Buy bananas')

        # When she hits enter, the page updates, and now the page lists:
        # "1: Buy bananas" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy bananas' for row in rows),
            "New to-do item did not appear in table."
        )

        # There is still a text box inviting her to add another item.
        # She enters "Make pie with bananas"
        self.fail('Finish the test!')

        # The page updates again, and now shows both items in her list

        # The site has generated a unique URL for her

        # She visits that URL - her to-do list is still there.


if __name__ == '__main__':
    unittest.main(warnings = 'ignore')


