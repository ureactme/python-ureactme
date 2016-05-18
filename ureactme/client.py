from __future__ import absolute_import
import requests
from . import models


class Client:
    def __init__(self, token, url='http://ureact.me'):
        self.token = token
        self.url = url

    def get_headers(self):
        return {"Content-Type": "application/json",
                "Authorization": "Token %s" % self.token}

    def get_object_list(self, modelcls, **filters):
        url = self.url + modelcls.API_ENDPOINT
        r = requests.get(url, params=filters, headers=self.get_headers())
        data = r.json()

        return models.ModelList(self, filters, data, modelcls)
