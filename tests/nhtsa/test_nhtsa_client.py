from tests import TestCase

from nhtsa import NHTSAClient


class TestNHTSAClient(TestCase):
    def test_create(self):
        client = NHTSAClient()

        self.assertIsNotNone(client)

    def test_create_custom_url(self):
        client = NHTSAClient(api_path='https://localhost')

        self.assertIsNotNone(client)
        self.assertEqual(client.api_path, 'https://localhost')
