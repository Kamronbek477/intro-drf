from django.test import TestCase

class SumViewTestCase(TestCase):
    def test_sum(self):

        a = 2
        b = 4
        url = f'/api/sum/?a={a}&b={b}'
        response = self.client.get(url)
        self.assertEqual(response.json(), {'sum':a+b})