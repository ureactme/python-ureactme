class Model:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class User(Model):
    pass


class Metric(Model):
    pass


class Point(Model):
    pass
