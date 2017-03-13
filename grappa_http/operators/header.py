# -*- coding: utf-8 -*-
import re
from .base import BaseOperator, Operator

# Little hack to extract the regexp object type
retype = type(re.compile(''))


class HeaderOperator(BaseOperator):
    """
    Asserts HTTP response header(s).

    Example::

        # Should style
        res | should.have.header('Content-Type').equal.to('application/json')

        # Should style - negation form
        res | should.not_have.header('Server').equal.to('nginx')

        # Expect style
        res | expect.to.have.header('server').equal.to('nginx')

        # Expect style - negation form
        res | expect.to_not.have.header('server').equal.to('nginx')
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('header', 'headers')

    # Operator keywords
    aliases = ('of', 'to', 'be', 'equal', 'match')

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a response that match header(s): "{value}"',
        'a response that does not match header(s): "{value}"',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a response with header(s): {value}',
    )

    def match_header(self, headers, key, value, includes=False):
        if key not in headers:
            return False, 'headers "{}" is not present'.format(key)

        if isinstance(value, retype) and not value.match(headers[key]):
            return False, 'header "{}" does not matches: "{}" <> "{}"'.format(
                key, value.pattern, headers[key]
            )

        if includes and value not in headers[key]:
            return False, 'header "{}" does not contain "{}" in "{}"'.format(
                key, value, headers[key]
            )

        if not includes and value and headers[key] != value:
            return False, 'header "{}" is not equal: "{}" != "{}"'.format(
                key, headers[key], value
            )

        return True, None

    def _match(self, res, headers, value=None, includes=False):
        # Set subject headers
        self.subject = res.headers

        if not headers:
            return False, ['header argument cannot be empty']

        if isinstance(headers, str):
            headers = [headers]

        # Set expected headers
        self.expected = headers

        # Stores error reasons and header values
        reasons = []
        values = []

        for header in headers:
            matches, reason = self.match_header(res.headers, header,
                                                value,  includes=includes)
            if not matches and reason:
                reasons.append(reason)

            header = res.headers.get(header)
            if header:
                values.append(header)

        # Stores if the tests passed
        passed = len(reasons) == 0

        # Assign match value
        if value is None:
            self.ctx.value = values[0] if len(values) == 1 else values

        return passed, reasons
