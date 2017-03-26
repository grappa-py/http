# -*- coding: utf-8 -*-
from functools import reduce
from .base import BaseOperator, Operator

try:
    from urlparse import urlparse, parse_qs
except ImportError:
    from urllib.parse import urlparse, parse_qs


class UrlBaseOperator(BaseOperator):
    """
    Base operator for URL part operators.
    """

    # Defines operator kind
    kind = Operator.Type.MATCHER

    # Show match diff on error
    show_diff = True

    # Enable raw reporting mode for this operator
    raw_mode = True

    def get_url(self, res):
        if isinstance(res, str):
            return res
        if hasattr(res, 'url'):
            return str(res.url)
        return None

    def parse_url(self, url):
        try:
            return urlparse(url)
        except:
            return None

    def compare(self, value):
        raise NotImplementedError('compare method must be implemented')

    def _match(self, res, value, **kw):
        # Get response url
        raw_url = self.get_url(res)
        if not raw_url:
            return False, ['cannot parse request URL']

        url = self.parse_url(raw_url)
        if not url:
            return False, ['url is empty or cannot be readed']

        # Expose fields
        self.subject = raw_url

        return self.compare(url, value, **kw)


class UrlProtocolOperator(UrlBaseOperator):
    """
    Asserts HTTP request target URL protocol scheme.

    Example::

        # Should style
        res | should.have.url.protocol('http')
        res | should.have.url.protocol('https')
        res | should.have.url.schema('http')
        res | should.have.url.schema('https')

        # Should style - negation form
        res | should.not_have.url.protocol('http')
        res | should.not_have.url.protocol('https')
        res | should.not_have.url.schema('http')
        res | should.not_have.url.schema('https')

        # Expect style
        res | expect.to.have.url.protocol('http')
        res | expect.to.have.url.protocol('https')
        res | expect.to.have.url.schema('http')
        res | expect.to.have.url.schema('https')

        # Expect style - negation form
        res | expect.to_not.have.url.protocol('http')
        res | expect.to_not.have.url.protocol('https')
        res | expect.to_not.have.url.schema('http')
        res | expect.to_not.have.url.schema('https')
    """

    # Defines operator kind
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('protocol', 'scheme')

    # Operator aliases
    aliases = ('equal', 'to', 'be')

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a request target URL protocol scheme equal to "{value}"',
        'a request target URL protocol scheme not equal to: "{value}"',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a request target URL with protocol scheme value "{value}"',
    )

    def compare(self, url, protocol):
        if not isinstance(protocol, str):
            return False, ['URL protocol schema must be a string']

        self.subject = url.scheme
        self.expected = protocol

        return protocol == url.scheme, ['Missmatched URL protocol value']


class UrlHostnameOperator(UrlBaseOperator):
    """
    Asserts HTTP request target URL hostname value.

    Example::

        # Should style
        res | should.have.url.hostname('foo.com')
        res | should.have.url.hostname('foo', strict=False)

        # Should style - negation form
        res | should.not_have.url.hostname('foo.com')
        res | should.not_have.url.hostname('foo', strict=False)

        # Expect style
        res | expect.to.have.url.hostname('foo.com')
        res | expect.to.have.url.hostname('foo', strict=False)

        # Expect style - negation form
        res | expect.to_not.have.url.hostname('foo.com')
        res | expect.to_not.have.url.hostname('foo', strict=False)
    """

    # Defines operator kind
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('hostname', 'host')

    # Operator aliases
    aliases = ('equal', 'to', 'be')

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a request target URL hostname equal to "{value}"',
        'a request target URL hostname not equal to: "{value}"',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a request target URL with hostname value "{value}"',
    )

    def compare(self, url, hostname, strict=True):
        if not isinstance(hostname, str):
            return False, ['URL hostname schema must be a string']

        self.subject = url.hostname
        self.expected = hostname

        if strict:
            return hostname == self.subject, ['Missmatched URL hostnames']
        else:
            return (hostname in self.subject,
                    ['URL hostname does not contain "{}"'.format(hostname)])


class UrlPortOperator(UrlBaseOperator):
    """
    Asserts HTTP request target URL port value.

    Example::

        # Should style
        res | should.have.url.port(80)

        # Should style - negation form
        res | should.not_have.url.port(80)

        # Expect style
        res | expect.to.have.url.port(80)

        # Expect style - negation form
        res | expect.to_not.have.url.port(80)
    """

    # Defines operator kind
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('port',)

    # Operator aliases
    aliases = ('equal', 'to', 'be', 'number')

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a request target URL port equal to "{value}"',
        'a request target URL port not equal to: "{value}"',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a request target URL with port number "{value}"',
    )

    def compare(self, url, port):
        if not isinstance(port, int):
            return False, ['URL port must be an int']

        self.subject = url.port or (443 if url.scheme == 'https' else 80)
        self.expected = port

        return port == self.subject, ['Missmatched URL ports']


class UrlPathOperator(UrlBaseOperator):
    """
    Asserts HTTP request target URL path value.

    Example::

        # Should style
        res | should.have.url.path('/foo/baz')
        res | should.have.url.path('foo', strict=False)

        # Should style - negation form
        res | should.not_have.url.path('/foo/baz')
        res | should.not_have.url.path('foo', strict=False)

        # Expect style
        res | epect.to.have.url.path('/foo/baz')
        res | epect.to.have.url.path('foo', strict=False)

        # Expect style - negation form
        res | epect.to_not.have.url.path('/foo/baz')
        res | epect.to_not.have.url.path('foo', strict=False)
    """

    # Defines operator kind
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('path',)

    # Operator aliases
    aliases = ('equal', 'to', 'be')

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a request target URL path equal to "{value}"',
        'a request target URL path not equal to: "{value}"',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a request target URL with path value "{value}"',
    )

    def compare(self, url, path, strict=True):
        if not isinstance(path, str):
            return False, ['URL path must be a string']

        self.subject = url.path
        self.expected = path

        if strict:
            return path == self.subject, ['Missmatched URL path']
        else:
            return (path in self.subject,
                    ['URL path does not contain "{}"'.format(path)])


class UrlParamsOperator(UrlBaseOperator):
    """
    Asserts HTTP request target URL query params.

    Example::

        # Should style
        res | should.have.url.query({'foo': 'bar'})  # value
        res | should.have.url.query({'foo': True}) # presence
        res | should.have.url.query({'foo': 'b'}, strict=False) # contains

        # Should style - negation form
        res | should.not_have.url.query({'foo': 'bar'})  # value
        res | should.not_have.url.query({'foo': True}) # presence
        res | should.not_have.url.query({'foo': 'b'}, strict=False) # contains

        # Expect style
        res | expect.to.have.url.query({'foo': 'bar'})  # value
        res | expect.to.have.url.query({'foo': True}) # presence
        res | expect.to.have.url.query({'foo': 'b'}, strict=False) # contains

        # Expect style - negation form
        res | expect.to.have.url.query({'foo': 'bar'})  # value
        res | expect.to.have.url.query({'foo': True}) # presence
        res | expect.to.have.url.query({'foo': 'b'}, strict=False) # contains
    """

    # Defines operator kind
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('params', 'query')

    # Operator aliases
    aliases = ('to', 'be', 'params', 'string')

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a request target URL query params match to "{value}"',
        'a request target URL query params not match to: "{value}"',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a request URL with query params "{value}"',
    )

    def compare(self, url, query, strict=False):
        if isinstance(query, str):
            query = parse_qs(query)

        if not isinstance(query, dict):
            return False, ['URL query must be a dictionary or query string']

        self.subject = parse_qs(url.query)
        self.expected = query

        def match(key, value):
            compare = (lambda x, y: x == y) if strict else lambda x, y: x in y
            return any([
                True
                for _value in self.subject.get(key)
                if compare(value, _value)
            ])

        def validate(reasons, item):
            key, values = item
            values = [values] if not isinstance(values, list) else values

            if key not in self.subject:
                return reasons + ['query param "{}" not found'.format(key)]

            for value in values:
                if value is True:
                    continue

                if value is False:
                    return reasons + [
                        'query param "{}" is present'.format(key)]

                if not match(key, value):
                    reason = (
                        'query param "{}" is not to equal to "{}"'.format(
                            key, value
                        )
                    )
                    return reasons + [reason]

            return reasons

        reasons = reduce(validate, query.items(), [])
        return len(reasons) == 0, reasons
