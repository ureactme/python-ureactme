import requests


class Client:
    def __init__(self, token, url='http://ureact.me'):
        self.token = token
        self.url = url

    def get_headers(self):
        return {"Content-Type": "application/json",
                "Authorization": "Token %s" % self.token}
