# -*- coding: utf-8 -*-
import json
from .base import BaseOperator, Operator


class JsonOperator(BaseOperator):
    """
    Asserts HTTP response body JSON content.

    Example::

        # Should style
        res | should.have.json({'foo': 'bar'})
        res | should.have.json.equal.to({'foo': 'bar'})
        res | should.have.json(r'(\w+) world$')
        res | should.have.json.to.contain('world')

        # Should style - negation form
        res | should.not_have.json({'foo': 'bar'})
        res | should.not_have.json.equal.to({'foo': 'bar'})
        res | should.have.json.match.to(r'(\w+) world$')
        res | should.not_have.json.to.contain('world')

        # Expect style
        res | expect.to.have.json({'foo': 'bar'})
        res | expect.to.have.json.equal.to({'foo': 'bar'})
        res | expect.to.have.json.to.match(r'(\w+) world$')
        res | expect.to.have.json.to.contain('world')

        # Expect style - negation form
        res | expect.to_not.have.json({'foo': 'bar'})
        res | expect.to_not.have.json.equal.to({'foo': 'bar'})
        res | expect.to_not.have.json.to.match(r'(\w+) world$')
        res | expect.to_not.have.json.to.contain('world')
    """

    # Defines operator kind
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('json',)

    # Operator aliases
    aliases = ('equal', 'data', 'to', 'be')

    # Enable raw reporting mode for this operator
    raw_mode = True

    # Raw limit characters
    raw_size = 500

    # Show match diff on error
    show_diff = True

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a response JSON body equal to:\n    {value}',
        'a response JSON body not equal to:\n    {value}',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a response JSON body with data:\n    {value}',
    )

    def _on_access(self, res):
        if isinstance(res, str):
            self.ctx.subject = json.loads(res)
        else:
            self.ctx.subject = res.json

    def get_json(self, res):
        if isinstance(res, str):
            return json.loads(res)
        if isinstance(res, (dict, tuple)):
            return res
        else:
            return res.json

    def _match(self, res, expected):
        data = self.get_json(res)
        if data is None:
            return False, ['empty JSON response']

        # Read expected JSON as string
        if isinstance(expected, str):
            expected = json.loads(expected)
        else:
            self.diff_expected = json.dumps(expected, indent=4)
            # Re-deserialize JSON to have full unicode compatibility
            expected = json.loads(self.diff_expected)

        if data is None:
            return False, ['invalid body response: cannot read JSON']

        self.diff_subject = json.dumps(data, indent=4)
        if hasattr(self.diff_subject, 'decode'):  # Python 2
            self.diff_subject = self.diff_subject.decode('ascii')

        self.subject = data
        return data == expected, ['missmatched JSON bodies']
