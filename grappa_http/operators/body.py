# -*- coding: utf-8 -*-
from .json import JsonOperator
from .base import BaseOperator, Operator


class BodyOperator(BaseOperator):
    """
    Asserts HTTP response body content as string.

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
    operators = ('body', 'data')

    # Operator aliases
    aliases = ('equal', 'to', 'be')

    # List of suboperators
    suboperators = (
        JsonOperator,
    )

    # Enable raw reporting mode for this operator
    raw_mode = True

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a response body data equal to: {value}',
        'a response body data not equal to: {value}',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a response body with data: {value}',
    )

    def _on_access(self, res):
        self.ctx.subject = res.body

    def get_body(self, res):
        if isinstance(res, str):
            return res
        if hasattr(res, 'body'):
            return res.body
        return None

    def _match(self, res, expected):
        self.ctx.show_diff = True

        # Get response body data
        body = self.get_body(res)

        if not isinstance(expected, str):
            return False, ['body expectation must be a string']

        if body is None:
            return False, ['body is empty or cannot be readed']

        if len(body) == 0:
            return False, ['body is empty']

        self.ctx.value = res.body
        self.subject = res.body
        self.expected = expected

        return expected == body, []