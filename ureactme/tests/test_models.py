from unittest import TestCase
from ureactme import models
import mock


class TestModelList(TestCase):
    def get_sample_data(self):
        return {"meta": {"total": 3,
                         "total_pages": 1,
                         "per_page": 100,
                         "page": 1},
                "data": [{"id": "foo:blauser",
                          "auto_data": None,
                          "data": None},
                         {"id": "fulano",
                          "auto_data": None,
                          "data": None},
                         {"id": "fao:blauser",
                          "auto_data": None,
                          "data": None}]}

    def test_len(self):
        data = self.get_sample_data()
        l = models.ModelList(None, data['meta'], data['data'], models.User)
        self.assertEqual(len(l), 3)
