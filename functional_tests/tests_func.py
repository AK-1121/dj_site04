#import selenium
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import unittest
import time


#class NewVisitorTest(unittest.TestCase):
class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        #self.browser = webdriver.Firefox()
        self.browser = webdriver.Chrome()
        #self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    # Helper method (help to implement DRY principle):
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith open home page of online to-do app:
        #self.browser.get('http://localhost:8000')
        self.browser.get(self.live_server_url)
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

        # Find number of <tr><td> to determine the number of elemets that
        # are already in to-do list:
        table = self.browser.find_element_by_id('id_list_table')
        recs_in_list = len(table.find_elements_by_tag_name('tr'))
        print('number of rows:', recs_in_list)

        # She types "Buy bananas" into a text box
        inputbox.send_keys('Buy bananas')

        # When she hits enter, the page updates, and now the page lists:
        # "1: Buy bananas" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table(str(recs_in_list+1) + ': Buy bananas')

        # There is still a text box inviting her to add another item.
        # She enters "Make pie with bananas"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Make pie with bananas')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items in her list
        self.check_for_row_in_list_table(str(recs_in_list+1) + ': Buy bananas')
        self.check_for_row_in_list_table(
            str(recs_in_list+2) + ': Make pie with bananas'
        )
        #table = self.browser.find_element_by_id('id_list_table')
        #rows = table.find_elements_by_tag_name('tr')
        #self.assertIn('1: Buy bananas', [row.text for row in rows])
        #self.assertIn('2: Make pie with bananas', [row.text for row in rows])

        # The site has generated a unique URL for her

        # She visits that URL - her to-do list is still there.
        self.fail('Finish the test!')

    '''
    def test_my_test(self):
        #self.browser.refresh()
        time.sleep(2)
        self.assertIn('To-do', self.browser.title)
    '''

# We started to use Django for running FT, so we commented out this part:
#if __name__ == '__main__':
#    unittest.main(warnings = 'ignore')


