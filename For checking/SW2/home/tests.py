from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class HomeTest(SimpleTestCase):
    def test_book_list_view_by_url(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
        self.assertContains(resp, 'Sweet home')
    
    def test_book_list_view_by_nickname(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
        self.assertContains(resp, 'Sweet home')