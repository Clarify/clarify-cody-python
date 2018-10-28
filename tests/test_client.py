import unittest
import httpretty
try:
    from urllib.parse import parse_qs
except ImportError:
     from urlparse import parse_qs
from clarify_cody.client import Client
# from clarify_cody.helpers import get_embedded, get_link_href
from . import register_uris


class TestClient(unittest.TestCase):

    def setUp(self):
        api_key = 'my-api-key'
        self.client = Client(api_key)

    def tearDown(self):
        self.client = None

    @httpretty.activate
    def test_create_conversation(self):
        register_uris(httpretty)
        conv = self.client.create_conversation(external_id="123")
        self.assertIsNotNone(conv)
        self.assertEqual(conv['external_id'], '123')
