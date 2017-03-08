from .base import BaseAdapter


class Urllib3Adapter(BaseAdapter):
    """
    Response adapter for `urllib3`.
    """

    @staticmethod
    def test(res):
        return False
