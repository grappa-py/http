from .base import BaseAdapter


class AioHttpAdapter(BaseAdapter):
    """
    Response adapter for `aiohttp`.
    """

    @staticmethod
    def test(res):
        return False
