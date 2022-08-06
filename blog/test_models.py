from django.test import TestCase


class TestBlogModels(TestCase):

    def test_get_absolute_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
