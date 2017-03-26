# -*- coding: utf-8 -*-
from .base import BaseOperator, Operator


class StatusOperator(BaseOperator):
    """
    Asserts HTTP response status code or name.

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

    # Show match diff on error
    show_diff = True

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
            return False, ['status must be an int, string or iterable']

        self.subject = res.status_code
        if isinstance(status, (tuple, list)) and len(status) == 2:
            start, end = status
            return self.subject >= start and self.subject <= end

        if isinstance(status, str):
            status = status.lower()
            self.subject = res.status.lower()

        return self.subject == status, []


class OkStatusOperator(StatusOperator):
    """
    Asserts HTTP response status is `OK`.

    Example::

        # Should style
        res | should.be.ok

        # Should style - negation form
        res | should.not_be.ok

        # Expect style
        res | expect.to.be.ok

        # Expect style - negation form
        res | expect.to_not.be.ok
    """

    # Is the operator a keyword
    kind = Operator.Type.ACCESSOR

    # Operator keywords
    operators = ('ok',)

    # Expected status code
    expected = '200'

    def _match(self, res):
        return StatusOperator._match(self, res, 200)


class ServerErrorStatusOperator(StatusOperator):
    """
    Asserts HTTP response status should be a server error (`500`-`599`).

    Example::

        # Should style
        res | should.be.server_error

        # Should style - negation form
        res | should.not_be.server_error

        # Expect style
        res | expect.to.be.server_error

        # Expect style - negation form
        res | expect.to_not.be.server_error
    """

    # Is the operator a keyword
    kind = Operator.Type.ACCESSOR

    # Operator keywords
    operators = ('server_error',)

    # Expected status code
    expected = '500-599'

    def _match(self, res):
        return StatusOperator._match(self, res, [500, 599])


class BadRequestStatusOperator(StatusOperator):
    """
    Asserts HTTP response status should be a server error (`400`-499`).

    Example::

        # Should style
        res | should.be.bad_request

        # Should style - negation form
        res | should.not_be.bad_request

        # Expect style
        res | expect.to.be.bad_request

        # Expect style - negation form
        res | expect.to_not.be.bad_request
    """

    # Is the operator a keyword
    kind = Operator.Type.ACCESSOR

    # Operator keywords
    operators = ('bad_request',)

    # Expected status code
    expected = '400-499'

    def _match(self, res):
        return StatusOperator._match(self, res, [400, 499])
