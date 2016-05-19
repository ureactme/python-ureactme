from __future__ import absolute_import
import requests
from .models import ModelList
import datetime
import json


class Client(object):
    def __init__(self, token=None, url=None):
        import ureactme
        if token is not None:
            ureactme.api_key = token

        if url is not None:
            ureactme.url = url

        self.token = token or ureactme.api_key
        self.url = url or ureactme.url

    def get_headers(self):
        return {"Content-Type": "application/json",
                "Authorization": "Token %s" % self.token}

    def post(self, url, data):
        requests.post(url, data, headers=self.get_headers())

    def send_event(self, metric, user, value=None, data=None, date=None):
        from ureactme.models import Event
        payload = {"date": date or datetime.datetime.now().isoformat(),
                   "metric": metric,
                   "user": user,
                   "value": value,
                   "data": data}
        url = self.url + Event.API_ENDPOINT
        r = requests.post(url, json.dumps(payload), headers=self.get_headers())
        if r.status_code > 299 or r.status_code < 200:
            raise ValueError(r.content)

    def get_object_list(self, modelcls, url=None, **filters):
        """
        Returns the list of objects using the given **kwargs as filters

        If url is not none, use this URL when fetching, instead
        of modelcls.API_ENDPOINT variable
        """
        if url is None:
            url = self.url + modelcls.API_ENDPOINT
        r = requests.get(url, params=filters, headers=self.get_headers())
        if r.status_code > 299 or r.status_code < 200:
            raise ValueError(r.content)
        data = r.json()

        return ModelList(self, filters, data, modelcls)
