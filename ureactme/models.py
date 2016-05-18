class Model:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class ModelList:
    def __init__(self, client, meta, objects, modelcls):
        self.client = client
        self.meta = meta
        self.objects = objects
        self.modelcls = modelcls

    def __len__(self):
        return self.meta['total']

    def __iter__(self):
        i = 0
        while True:
            if i < len(self.objects):
                yield self.modelcls(**self.objects[i])
                i += 1
            else:
                break


class User(Model):
    API_ENDPOINT = "/api/v2/user"


class Metric(Model):
    API_ENDPOINT = "/api/v2/metric"


class Point(Model):
    pass
