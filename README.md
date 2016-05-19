# UReact.me Python client

## Instalation

It's on pip. Just `pip install ureactme` and it's done.

## Usage

```python
from ureactme import Client
from ureactme.models import Metric, User, Event

c = Client("put your token here")

# Get the list of Metrics sent by users:
metrics = c.get_object_list(Metric)
for m in metrics:
  print m.id

# Get the list of Users, and print his ID, the data and the auto-collected data
users = c.get_object_list(User)
for u in users:
    print u.id, u.data, u.auto_data

# Get the list of events of a certain type sent by the user in a given day
u = User(id="user_id_test")
for e in u.get_events('redbutton_click', '2016-05-18'):
    print e.created_at, e.value, e.data


# Send an event
c.send_event("suggestion_click", "user_123", 10)

# Get detailed statistics for a given date range, for all users and metrics
print list(c.get_statistics(['2015-01-01', '2017-01-01']))
[{u'avg_value': 15.0,
  u'count': 1,
  u'day': u'2016-05-19',
  u'device_user': u'user1',
  u'max_value': 15.0,
  u'metric': u'login',
  u'min_value': 0.0,
  u'sum_value': 15.0},
 {u'avg_value': 15.0,
  u'count': 1,
  u'day': u'2016-05-19',
  u'device_user': u'user2',
  u'max_value': 15.0,
  u'metric': u'login',
  u'min_value': 0.0,
  u'sum_value': 15.0}]


# Get detailed user statistics (regardless of the metric)
c.get_statistics(['2015-01-01', '2017-01-01'], fields=["user"])
[{u'avg_value': 15.0,
  u'count': 1,
  u'device_user': u'user1',
  u'max_value': 15.0,
  u'min_value': 0.0,
  u'sum_value': 15.0},
 {u'avg_value': 15.0,
  u'count': 2,
  u'device_user': u'user2',
  u'max_value': 15.0,
  u'min_value': 0.0,
  u'sum_value': 30.0}]

# Get detailed metric statistics per day (regardless of the user)
print list(c.get_statistics(['2015-01-01', '2017-01-01'], fields=["metric", "day"]))
[{u'avg_value': 15.0,
  u'count': 3,
  u'day': u'2016-05-19',
  u'max_value': 15.0,
  u'metric': u'login',
  u'min_value': 0.0,
  u'sum_value': 45.0},
 {u'avg_value': 13.75,
  u'count': 4,
  u'day': u'2016-05-19',
  u'max_value': 15.0,
  u'metric': u'suggestion_click',
  u'min_value': 0.0,
  u'sum_value': 55.0}]

```
