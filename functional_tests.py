from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_lists_and_retrieve_it_later(self):
        # check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page gtitle and header mention to-do lists
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's how
        # is typing fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #     any(row.text == '1: Buy peacock feathers' for row in rows),
        #     f"new to-do item did not appear in table. Contents were:\n{table.text}"
        # )

        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])
        # There is still a text box inviting her to add another item.
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
        # self.fail('Finish the test!')
        # The page updates again, and now shows both items on her list

        # Edith wonders wheter the site will remember her list. Then she sees
        # theat the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She vists that URL - her to-do list is sitll there.

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
