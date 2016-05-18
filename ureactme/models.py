class Model:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class ModelList:
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


class Metric(Model):
    API_ENDPOINT = "/api/v2/metric"


class Point(Model):
    pass
