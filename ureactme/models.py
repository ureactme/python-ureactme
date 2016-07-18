from __future__ import absolute_import
from dateutil.parser import parse as parse_datetime


class Model(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def get_by_id(cls, id):
        from . import client
        return list(client.Client().get_object_list(cls, id__eq=id))[0]

    @classmethod
    def get_list(cls, **filter):
        from . import client
        return client.Client().get_object_list(cls, **filter)


class ModelList(object):
    def __init__(self, client, filters, payload, modelcls):
        self.client = client
        self.filters = filters
        self.meta = payload['meta']
        self.objects = payload['data']
        self.modelcls = modelcls

    def __len__(self):
        return self.meta['total']

    def __iter__(self):
        i = 0
        while True:
            if i < len(self.objects):
                yield self.modelcls(**self.objects[i])
                i += 1
            elif self.meta['page'] < self.meta['total_pages']:
                # get next page
                filters = self.filters.copy()
                filters['page'] = self.meta['page'] + 1
                for k in self.client.get_object_list(self.modelcls, **filters):
                    yield k
                break
            else:
                break


class User(Model):
    API_ENDPOINT = "/api/v2/user"

    def get_events(self, metric, date):
        from . import client
        metric_id = metric.id if isinstance(metric, Metric) else metric
        filters = {"metric": metric_id, "user": self.id, "day": date}
        return client.Client().get_object_list(Event, **filters)

    def __str__(self):
        return self.id


class Metric(Model):
    API_ENDPOINT = "/api/v2/metric"

    def __str__(self):
        return self.id


class Event(Model):
    API_ENDPOINT = "/api/v2/event"

    def __init__(self, **kwargs):
        super(Event, self).__init__(**kwargs)
        if isinstance(self.created_at, basestring):
            self.created_at = parse_datetime(self.created_at)

    def __str__(self):
        return "%s (%s; %s)" % (self.created_at, self.value, self.data)


class DayStatistic(Model):
    API_ENDPOINT = '/api/v2/stats'
