from .base import BaseAdapter


class RequestsAdapter(BaseAdapter):
    """
    Adapter for `requests` HTTP client.
    """

    def __init__(self, res):
        self.res = res

    @staticmethod
    def test(res):
        if not res:
            return False

        return all([
            'requests' in res.__module__,
            res.__class__.__name__ == 'Response'
        ])

    @property
    def status(self):
        return self.res.reason

    @property
    def status_code(self):
        return self.res.status_code

    @property
    def url(self):
        return self.res.url

    @property
    def request(self):
        return self.res.request

    @property
    def headers(self):
        return self.res.headers

    @property
    def body(self):
        return self.res.body()

    @property
    def json(self):
        return self.res.json(indent=4)

    @property
    def elapsed(self):
        return self.res.elapsed

    @property
    def encoding(self):
        return self.res.encoding
