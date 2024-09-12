from requests import api
from requests.auth import HTTPBasicAuth


class OfferApiSYNC:
    def __init__(self, auth: HTTPBasicAuth, url: str, data: list | dict, data_type: str = 'json', success_code: int = 200):
        self.auth: HTTPBasicAuth = auth
        self.url: str = url
        self.data: list | dict = data
        self.data_type: str = data_type
        self.success_code: int = success_code
        self.status: bool = False
        self.sync()

    def sync(self):
        payload: dict = {'auth': self.auth, 'url': self.url, 'json' if self.data_type == 'json' else 'data': self.data}
        response = api.post(**payload)
        self.status = response.status_code == self.success_code

    def __bool__(self):
        return self.status
