from django.test import SimpleTestCase

# Create your tests here.

class SimpleTeste(SimpleTestCase):
    def test_home_page_by_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_by_url(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
    def test_index_page_by_url(self):
        resp = self.client.get('/index/')
        self.assertEqual(resp.status_code, 200)