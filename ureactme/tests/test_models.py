from unittest import TestCase
from ureactme import models
import mock


class TestModelList(TestCase):

    def test_len(self):
        data = {"meta": {"total": 3,
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
        l = models.ModelList(None, {}, data, models.User)
        self.assertEqual(len(l), 3)

    def test_iteration_single_page(self):
        data = {"meta": {"total": 3,
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

        l = models.ModelList(None, {}, data, models.User)
        self.assertTrue(all(isinstance(i, models.User) for i in l))

    def test_iteration_get_next_page(self):
        data = {"meta": {"total": 4,
                         "total_pages": 2,
                         "per_page": 3,
                         "page": 1},
                "data": [{"id": "user1",
                          "auto_data": None,
                          "data": None},
                         {"id": "user2",
                          "auto_data": None,
                          "data": None},
                         {"id": "user3",
                          "auto_data": None,
                          "data": None}]}

        # second page
        data2 = {"meta": {"total": 4,
                          "total_pages": 1,
                          "per_page": 100,
                          "page": 1},
                 "data": [{"id": "user4",
                           "auto_data": None,
                           "data": None}]}

        # client returns the next list
        client = mock.Mock()
        second_page_list = models.ModelList(client, {}, data2, models.User)
        client.get_object_list.return_value = second_page_list
        l = models.ModelList(client, {}, data, models.User)

        self.assertEqual([i.id for i in l],
                         ["user1", "user2", "user3", "user4"])
