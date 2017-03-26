# -*- coding: utf-8 -*-
from .base import BaseOperator, Operator
from .url_parts import (UrlProtocolOperator, UrlHostnameOperator,
                        UrlPortOperator, UrlPathOperator, UrlParamsOperator)


class UrlOperator(BaseOperator):
    """
    Asserts HTTP request target URL.

    Example::

        # Should style
        res | should.have.body('hello world')
        res | should.have.body.equal.to('hello world')
        res | should.have.body.match.to(r'(\w+) world$')
        res | should.have.body.to.contain('world')

        # Should style - negation form
        res | should.not_have.body('hello world')
        res | should.not_have.body.equal.to('hello world')
        res | should.have.body.match.to(r'(\w+) world$')
        res | should.not_have.body.to.contain('world')

        # Expect style
        res | expect.to.have.body('hello world')
        res | expect.to.have.body.equal.to('hello world')
        res | expect.to.have.body.to.match(r'(\w+) world$')
        res | expect.to.have.body.to.contain('world')

        # Expect style - negation form
        res | expect.to_not.have.body('hello world')
        res | expect.to_not.have.body.equal.to('hello world')
        res | expect.to_not.have.body.to.match(r'(\w+) world$')
        res | expect.to_not.have.body.to.contain('world')
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
            self.ctx.subject = res.url

    def get_url(self, res):
        if isinstance(res, str):
            return res
        if hasattr(res, 'url'):
            return res.url
        return None

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
