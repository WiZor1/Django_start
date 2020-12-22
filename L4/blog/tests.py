from django.test import TestCase
from django.urls import reverse
from .models import Post
from django.contrib.auth import get_user_model

# Create your tests here.

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@test.com',
            password = 'testpass',
        )

        self.post = Post.objects.create(
            title = 'Test title',
            body = 'Test body',
            author = self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.post), 'Test title')

    def test_post_right_content(self):
        self.assertEqual(str(self.post.title), 'Test title')
        self.assertEqual(str(self.post.body), 'Test body')
        self.assertEqual(str(self.post.author), 'testuser')

    def test_post_list_view_by_url(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
        self.assertContains(resp, 'Test body')

    def test_post_list_view_by_nickname(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
        self.assertContains(resp, 'Test body')
    
    def test_post_detail_view(self):
        resp = self.client.get('/post/1/')
        no_resp = self.client.get('/post/10000000000/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(no_resp.status_code, 404)