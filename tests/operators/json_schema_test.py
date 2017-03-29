import pook
import pytest
import requests


def test_json_schema_operator(should):
    schema = {
        'type': 'object',
        'properties': {
            'price': {'type': 'number'},
            'name': {'type': 'string'}
        }
    }

    with pook.use():
        pook.get('foo.com').reply(200).json({'name': 'Eggs', 'price': 34.99})
        res = requests.get('http://foo.com')
        res | should.satisfy.json_schema(schema)


def test_json_schema_error(should):
    schema = {
        'type': 'object',
        'properties': {
            'price': {'type': 'number'},
            'name': {'type': 'number'}
        }
    }

    with pook.use():
        pook.get('foo.com').reply(200).json({'name': 'Eggs', 'price': True})
        res = requests.get('http://foo.com')

        with pytest.raises(AssertionError):
            res | should.satisfy.json_schema(schema)
