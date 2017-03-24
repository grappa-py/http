from abc import ABCMeta, abstractproperty


class BaseAdapter(object):
    """
    BaseAdapter implements.
    """

    # Metaclass definition for Python 2 compatibility
    __metaclass__ = ABCMeta

    @abstractproperty
    def method(self):
        pass

    @abstractproperty
    def status(self):
        pass

    @abstractproperty
    def status_code(self):
        pass

    @abstractproperty
    def url(self):
        pass

    @abstractproperty
    def request(self):
        pass

    @abstractproperty
    def headers(self):
        pass

    @abstractproperty
    def body(self):
        pass

    @abstractproperty
    def json(self):
        pass

    @abstractproperty
    def encoding(self):
        pass

    @abstractproperty
    def cookies(self):
        pass

    @abstractproperty
    def elapsed(self):
        pass

    def __repr__(self):
        return '{}({} {} | {})'.format(
            'HttpResponse',
            self.method,
            self.url,
            self.headers
        )
