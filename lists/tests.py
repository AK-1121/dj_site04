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
        #self.assertEqual(response.content.decode(), expected_html)  # string
        # comparison
        self.assertEqual(response.content, expected_html.encode())  # byte comparison

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new item list'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)

    def test_home_page_displays_all_list_items(self):
        Item.objects.create(text='item_text 1')
        Item.objects.create(text='item_text 2')

        request = HttpRequest()
        response = home_page(request)

        self.assertIn('item_text 1', response.content.decode())
        self.assertIn('item_text 2'.encode(), response.content)

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



