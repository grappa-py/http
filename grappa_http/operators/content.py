# -*- coding: utf-8 -*-
from .header import HeaderOperator
from .base import BaseOperator, Operator


# Content type aliases
ALIASES = {
    'html': 'text/html',
    'json': 'application/json',
    'xml': 'application/xml',
    'urlencoded': 'application/x-www-form-urlencoded',
    'form': 'application/x-www-form-urlencoded',
    'form-data': 'application/x-www-form-urlencoded'
}


class ContentTypeOperator(BaseOperator):
    """
    Asserts HTTP response content type header value.

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
        res | expect.to.have.response.content.equal.to('application/json')

        # Expect style - negation form
        res | expect.to.not_have.content('json')
        res | expect.to.not_have.content.of('xml')
        res | expect.to.not_have.content.type('html')
        res | expect.to_not.have.response.content.equal.to('application/json')
    """

    # Defines operator kind
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('content', 'ctype')

    # Operator aliases
    aliases = ('type', 'equal', 'to', 'be', 'of')

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a response content type that matches with "{value}"',
        'a response content type that does not match with "{value}"',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a response content type equal to "{value}"',
    )

    def _match(self, res, content):
        if not content:
            return False, ['content type argument cannot be empty']

        if isinstance(content, str):
            content = ALIASES.get(content, content)

        self.expected = content
        self.subject = res.headers.get('Content-Type')

        operator = HeaderOperator(self.ctx)
        return operator.match(res, 'Content-Type', content, includes=True)
