# -*- coding: utf-8 -*-
from .base import BaseOperator, Operator


class MethodOperator(BaseOperator):
    """
    Asserts HTTP request method.

    Example::

        # Should style
        res | should.be.method('GET')

        # Should style - negation form
        res | should.not_be.method('GET')

        # Expect style
        res | expect.to.be.method('GET')

        # Expect style - negation form
        res | expect.to_not.be.method('GET')
    """

    # Defines operator kind
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('method', 'verb')

    # Operator aliases
    aliases = ('name', 'equal', 'to', 'be', 'of')

    # Show match diff on error
    show_diff = True

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a request method that is equal to "{value}"',
        'a request method that is not equal to "{value}"',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a request method "{value}"',
    )

    def _match(self, res, method):
        # Define subject as request method
        self.subject = res.method

        if not isinstance(method, str):
            return False, ['method argument must be a string']

        if not method:
            return False, ['method argument cannot be empty']

        return method.upper() == res.method, ['request method does not match']
