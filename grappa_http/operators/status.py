# -*- coding: utf-8 -*-
from .base import BaseOperator, Operator


class StatusOperator(BaseOperator):
    """
    Asserts if a given subject is `True` value.

    Example::

        # Should style
        res | should.be.status(200)

        # Should style - negation form
        res | should.not_be.status(200)

        # Expect style
        res | expect.to.be.status(200)

        # Expect style - negation form
        res | expect.to_not.be.status(200)
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('status',)

    # Operator keywords
    aliases = ('equal', 'to', 'be')

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a response status equal to {value}',
        'a response status not equal to {value}',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a response status equal to {value}',
    )

    def _match(self, res, status):
        if not status:
            return False, ['status must be an int or string']

        self.subject = res.status_code
        if isinstance(status, str):
            self.subject = res.status

        return self.subject == status, []
