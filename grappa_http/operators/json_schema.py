# -*- coding: utf-8 -*-
import json
from jsonschema import Draft4Validator
from .base import BaseOperator, Operator


class JsonSchemaOperator(BaseOperator):
    """
    Asserts HTTP response body JSON against a JSONSchema.

    Example::

        # Should style
        res | should.have.json_schema({'foo': 'bar'})
        res | should.have.json_schema({'foo': 'bar'})

        # Should style - negation form
        res | should.not_have.json({'foo': 'bar'})
        res | should.not_have.json.equal.to({'foo': 'bar'})

        # Expect style
        res | expect.to.have.json({'foo': 'bar'})
        res | expect.to.have.json.equal.to({'foo': 'bar'})

        # Expect style - negation form
        res | expect.to_not.have.json({'foo': 'bar'})
        res | expect.to_not.have.json.equal.to({'foo': 'bar'})
    """

    # Defines operator kind
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('json_schema', 'jsonschema')

    # Operator aliases
    aliases = ('equal', 'to', 'be')

    # Enable raw reporting mode for this operator
    raw_mode = True

    # Show match diff on error
    show_diff = True

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a response JSON body that matches the JSONSchema: {value}',
        'a response JSON body that does not matches the JSONSchem: {value}',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a JSON body with data: {value}',
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

    def validate_json(self, json, schema):
        errors = []
        v = Draft4Validator(schema)

        for error in sorted(v.iter_errors(json), key=str):
            errors.append('=> ' + str(error))

        if len(errors) == 0:
            return True

        err = AssertionError('\n\n'.join(errors))
        err.reasons = ['JSONSchema validation failed for the reasons above']
        raise err

    def _match(self, res, schema):
        data = self.get_json(res)
        self.ctx.show_diff = False

        if not schema:
            return False, ['JSONSchema value cannot be empty']

        if not isinstance(schema, (dict, str)):
            return False, ['JSONSchema must be a dict or str']

        # Read expected JSON as string
        if isinstance(schema, str):
            schema = json.loads(schema)
        else:
            self.expected = json.dumps(schema, indent=4)

        if data is None:
            return False, ['invalid body response: cannot read JSON']

        self.subject = json.dumps(data, indent=4)
        return self.validate_json(data, schema), []
