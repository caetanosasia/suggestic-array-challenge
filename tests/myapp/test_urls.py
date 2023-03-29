from django.test import Client, TestCase


class UrlsTestCase(TestCase):

    def test_normalize_array(self):
        response = Client().post('/normalize-array/', { 'input': [1, 2, [3, 4, [5, 6], 7], 8, 10], }, content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_admin_url(self):
        response = Client().get('/admin/', follow=True)
        self.assertEqual(response.status_code, 200)
