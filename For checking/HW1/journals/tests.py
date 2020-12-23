from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Journal

# Create your tests here.

class JournalTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'test_name',
            password = 'test_password',
        )

        self.journal = Journal.objects.create(
            title = 'Test_title',
            editor = 'Test_editor',
            pages_count = 321,
        )


    def test_journal_object_to_str(self):
        self.assertEqual(str(self.journal), 'Test_title')

    def test_journal_correct_content(self):
        self.assertEqual(str(self.journal.title), 'Test_title')
        self.assertEqual(str(self.journal.editor), 'Test_editor')
        self.assertEqual(int(self.journal.pages_count), 321)

    def test_journal_list_view_by_url(self):
        resp = self.client.get('/journals/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'journals.html')
        self.assertContains(resp, 'Test_title')
    
    def test_journal_list_view_by_nickname(self):
        resp = self.client.get(reverse('journals'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'journals.html')
        self.assertContains(resp, 'Test_title')
    
    def test_journal_res_list_view_by_url(self):
        resp = self.client.get('/journals/journals_reserved/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'journals_reserved.html')
        self.assertContains(resp, 'Test_title')
    
    def test_journal_res_list_view_by_nickname(self):
        resp = self.client.get(reverse('journals_reserved'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'journals_reserved.html')
        self.assertContains(resp, 'Test_title')
    
    def test_journal_list_detail_view(self):
        resp = self.client.get('/journals/journal/1/')
        not_found_resp = self.client.get('/journals/journal/99999999/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(not_found_resp.status_code, 404)