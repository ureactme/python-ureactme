from unittest import TestCase
from ureactme import client
import mock


class TestClient(TestCase):
    def test_get_header(self):
        c = client.Client("token123")
        self.assertEqual(c.get_headers(), {"Content-Type": "application/json",
                                           "Authorization": "Token token123"})
