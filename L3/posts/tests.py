from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='test text')

    def test_text_content(self):
        current_post = Post.objects.get(id=1)
        current_text = current_post.text
        exp_text = 'test text'
        self.assertEqual(current_text, exp_text)

class HomePageViewTest(TestCase):
    def test_view_by_url(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_by_nickname(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_with_template(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')