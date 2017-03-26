# -*- coding: utf-8 -*-
from .base import Operator
from .url_parts import (UrlProtocolOperator, UrlHostnameOperator,
                        UrlPortOperator, UrlPathOperator,
                        UrlParamsOperator, UrlBaseOperator)


class UrlOperator(UrlBaseOperator):
    """
    Asserts HTTP request target URL.

    Example::

        # Should style
        res | should.have.url('http://foo.org')
        res | should.have.url('foo.org', strict=False)
        res | should.have.url.hostname('foo.org')
        res | should.have.url.port(80)
        res | should.have.url.protocol('http')
        res | should.have.url.path('/bar/baz')
        res | should.have.url.query({'x': 'y', 'z': True})

        # Should style - negation form
        res | should.not_have.url('http://foo.org')
        res | should.not_have.url('foo.org', strict=False)
        res | should.not_have.url.hostname('foo.org')
        res | should.not_have.url.port(80)
        res | should.not_have.url.protocol('http')
        res | should.not_have.url.path('/bar/baz')
        res | should.not_have.url.query({'x': 'y', 'z': True})

        # Expect style
        res | expect.to.have.url('http://foo.org')
        res | expect.to.have.url('foo.org', strict=False)
        res | expect.to.have.url.hostname('foo.org')
        res | expect.to.have.url.port(80)
        res | expect.to.have.url.protocol('http')
        res | expect.to.have.url.path('/bar/baz')
        res | expect.to.have.url.query({'x': 'y', 'z': True})

        # Expect style - negation form
        res | expect.to_not.have.url('http://foo.org')
        res | expect.to_not.have.url('foo.org', strict=False)
        res | expect.to_not.have.url.hostname('foo.org')
        res | expect.to_not.have.url.port(80)
        res | expect.to_not.have.url.protocol('http')
        res | expect.to_not.have.url.path('/bar/baz')
        res | expect.to_not.have.url.query({'x': 'y', 'z': True})
    """

    # Defines operator kind
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('url',)

    # Operator aliases
    aliases = ('equal', 'to', 'be')

    # Supported suboperators
    suboperators = (
        UrlProtocolOperator,
        UrlHostnameOperator,
        UrlPathOperator,
        UrlParamsOperator,
        UrlPortOperator,
    )

    # Show match diff on error
    show_diff = True

    # Enable raw reporting mode for this operator
    raw_mode = True

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a request target URL equal to: {value}',
        'a request target URL not equal to: {value}',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a request target URL with value: {value}',
    )

    def _on_access(self, res):
        if hasattr(res, 'url'):
            self.ctx.subject = str(res.url)

    def _match(self, res, expected, strict=False):
        # Get response url data
        url = self.get_url(res)

        if not isinstance(expected, str):
            return False, ['URL expectation must be a string']

        if url is None:
            return False, ['url is invalid or cannot be readed']

        if len(url) == 0:
            return False, ['url is empty']

        self.subject = res.body
        self.expected = expected

        if strict:
            return expected == url, ['URLs are not equal']
        else:
            return expected in url, ['"{}" cannot be found in URL: {}'.format(
                expected, url
            )]
