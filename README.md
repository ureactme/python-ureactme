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
```
