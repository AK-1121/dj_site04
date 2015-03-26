from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
import datetime

from lists.views import home_page

from lists.models import Item

# Create your tests here.

class HomePageTest(TestCase):
    def test_root_url_resolvers_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('lists/home.html')
        #self.assertEqual(response.content.decode(), expected_html)  # string comparison
        self.assertEqual(response.content, expected_html.encode())  # byte comparison
        #self.assertTrue(response.content.startswith(b'<html>'))
        #self.assertIn(b'<title>To-Do lists</title>', response.content)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)
        expected_html = render_to_string(
            'lists/home.html',
            {'new_item_text': 'A new list item'}
        )
        self.assertEqual(response.content.decode(), expected_html)


class ItemModelTest():
    def __init__(self, TestCase):
        self.time_stamp0 = datetime.datetime.now() # for check DateTimeField

    def test_saving_and_retrieving_items(self):
        #time_stamp0 = datetime.datetime.now()
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
        print("Time:", time_stamp0, "\n", 
              first_saved_item.date.replace(tzinfo=None), "\n",
              datetime.datetime.now())
        # Check date and time of of to-do item in the base:
        self.assertTrue(
            self.time_stamp0 <= first_saved_item.date.replace(tzinfo=None) <=
            datetime.datetime.now()
        )

        #print("DB date:", first_saved_item.date)
        #print("DB date (tz=None):", first_saved_item.date.replace(tzinfo=None))
        #print("Time now:", datetime.datetime.now())
        #self.assertTrue(first_saved_item.date <= datetime.datetime.now())
    


