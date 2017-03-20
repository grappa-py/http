import pook
import pytest
import requests


@pook.on
def test_json_schema_operator(should):
    schema = {
        'type': 'object',
        'properties': {
            'price': {'type': 'number'},
            'name': {'type': 'string'}
        }
    }
    pook.get('foo.com').reply(200).json({'name': 'Eggs', 'price': 34.99})
    res = requests.get('http://foo.com')

    res | should.have.json_schema(schema)


@pook.on
def test_json_schema_error(should):
    schema = {
        'type': 'object',
        'properties': {
            'price': {'type': 'number'},
            'name': {'type': 'number'}
        }
    }
    pook.get('foo.com').reply(200).json({'name': 'Eggs', 'price': True})
    res = requests.get('http://foo.com')

    with pytest.raises(AssertionError):
        res | should.have.json_schema(schema)
