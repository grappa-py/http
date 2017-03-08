from .aiohttp import AioHttpAdapter
from .requests import RequestsAdapter

# Export symbols
__all__ = ('adapters', 'match')


# Adapters
adapters = (
    AioHttpAdapter,
    RequestsAdapter
)


def match(res):
    """
    Match adapter based on subject value
    """
    for adapter in adapters:
        if adapter.test(res):
            return adapter
