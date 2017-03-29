# -*- coding: utf-8 -*-
from .json_body import JsonOperator
from .json_schema import JsonSchemaOperator
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

    # Show match diff on error
    show_diff = True

    # Enable raw reporting mode for this operator
    raw_mode = True

    # Limit raw size characters
    raw_size = 500

    # List of suboperators
    suboperators = (
        JsonOperator,
        JsonSchemaOperator,
    )

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a response body data equal to:\n    {value}',
        'a response body data not equal to:\n    {value}',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a response body with data:\n    {value}',
    )

    def _on_access(self, res):
        if hasattr(res, 'body'):
            self.ctx.subject = str(res.body)

    def get_body(self, res):
        if isinstance(res, str):
            return res
        if hasattr(res, 'body'):
            return str(res.body)
        return None

    def _match(self, res, expected):
        # Get response body data
        body = self.get_body(res)

        if not isinstance(expected, str):
            return False, ['body expectation must be a string']

        if body is None:
            return False, ['body is empty or cannot be readed']

        if len(body) == 0:
            return False, ['body is empty']

        self.subject = res.body
        self.expected = expected

        return expected == body, []
