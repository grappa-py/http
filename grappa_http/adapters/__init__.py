from .base import BaseAdapter
from .aiohttp import AioHttpAdapter
from .requests import RequestsAdapter

# Module symbols to export
__all__ = (
    'adapters', 'match', 'use_adapter',
    'BaseAdapter', 'RequestsAdapter', 'AioHttpAdapter',
)


# List of supported HTTP adapters
adapters = (
    AioHttpAdapter,
    RequestsAdapter
)


def match(res):
    """
    Match adapter based on response object using type inference.

    Arguments:
        res (mixed): HTTP client specific response object to infer.

    Returns:
        grappa_http.adapters.BaseAdapter
    """
    for adapter in adapters:
        if adapter.test(res):
            return adapter


def use_adapter(*_adapters):
    """
    Adds one or multiple custom HTTP client adapters for
    testing introspection.

    Arguments:
        *adapters (grappa_http.BaseAdapter): adapter or adapters to use.
    """
    for adapter in _adapters:
        if not issubclass(adapter, BaseAdapter):
            raise TypeError('adapter must inherit from '
                            'grappa_http.BaseAdapter')

    global adapters
    adapters = _adapters + adapters
