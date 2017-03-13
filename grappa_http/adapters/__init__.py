from .base import BaseAdapter
from .aiohttp import AioHttpAdapter
from .requests import RequestsAdapter

# Module symbols to export
__all__ = ('adapters', 'match', 'BaseAdapter')


# List of supported HTTP adapters
adapters = (
    AioHttpAdapter,
    RequestsAdapter
)


def match(res):
    """
    Match adapter based on response object using type inference.
    """
    for adapter in adapters:
        if adapter.test(res):
            return adapter
