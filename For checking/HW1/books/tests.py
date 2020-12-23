from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Book

# Create your tests here.

class BookTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'test_name',
            password = 'test_password',
        )

        self.book = Book.objects.create(
            title = 'Test_title',
            author = 'Test_author',
            rating = 3,
        )

    def test_book_object_to_str(self):
        self.assertEqual(str(self.book), 'Test_title')

    def test_book_correct_content(self):
        self.assertEqual(str(self.book.title), 'Test_title')
        self.assertEqual(str(self.book.author), 'Test_author')
        self.assertEqual(int(self.book.rating), 3)

    def test_book_list_view_by_url(self):
        resp = self.client.get('/books/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'books.html')
        self.assertContains(resp, 'Test_title')
    
    def test_book_list_view_by_nickname(self):
        resp = self.client.get(reverse('books'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'books.html')
        self.assertContains(resp, 'Test_title')
    
    def test_book_res_list_view_by_url(self):
        resp = self.client.get('/books/books_reserved/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'books_reserved.html')
        self.assertContains(resp, 'Test_title')
    
    def test_book_res_list_view_by_nickname(self):
        resp = self.client.get(reverse('books_reserved'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'books_reserved.html')
        self.assertContains(resp, 'Test_title')
    
    def test_book_list_detail_view(self):
        resp = self.client.get('/books/book/1/')
        not_found_resp = self.client.get('/books/book/99999999/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(not_found_resp.status_code, 404)