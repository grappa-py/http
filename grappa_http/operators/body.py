# -*- coding: utf-8 -*-
from .base import BaseOperator, Operator


class BodyOperator(BaseOperator):
    """
    Asserts HTTP response body content.

    Example::

        # Should style
        res | should.be.content('json')
        res | should.be.content.of('xml')
        res | should.have.response.content.type('html')
        res | should.have.response.content.type('application/json')
        res | should.have.response.content.equal.to('application/json')

        # Should style - negation form
        res | should.not_have.content('json')
        res | should.not_have.content.of('json')

        # Expect style
        res | expect.to.have.content('json')
        res | expect.to.have.content.of('xml')
        res | expect.to.have.content.type('html')

        # Expect style - negation form
        res | expect.to.not_have.content('json')
        res | expect.to.not_have.content.of('xml')
        res | expect.to.not_have.content.type('html')
    """

    # Defines operator kind
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('body', 'data')

    # Operator aliases
    aliases = ('equal', 'to', 'be', 'of')

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a response content type that matches with "{value}"',
        'a response content type that does not match with "{value}"',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a response content type equal to "{value}"',
    )

    def _match(self, res, expected):
        self.ctx.show_diff = True
        self.ctx.value = res.body

        return expected == res.body, []


class JsonOperator(BaseOperator):
    """
    Asserts HTTP response body content.

    Example::

        # Should style
        res | should.be.content('json')
        res | should.be.content.of('xml')
        res | should.have.response.content.type('html')
        res | should.have.response.content.type('application/json')
        res | should.have.response.content.equal.to('application/json')

        # Should style - negation form
        res | should.not_have.content('json')
        res | should.not_have.content.of('json')

        # Expect style
        res | expect.to.have.content('json')
        res | expect.to.have.content.of('xml')
        res | expect.to.have.content.type('html')

        # Expect style - negation form
        res | expect.to.not_have.content('json')
        res | expect.to.not_have.content.of('xml')
        res | expect.to.not_have.content.type('html')
    """

    # Defines operator kind
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('json', 'json_body')

    # Operator aliases
    aliases = ('equal', 'to', 'be', 'of')

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a response content type that matches with "{value}"',
        'a response content type that does not match with "{value}"',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a response content type equal to "{value}"',
    )

    def _match(self, res, expected):
        self.ctx.show_diff = True
        self.ctx.value = res.json

        return res.json == expected, ['invalid json bodies']
