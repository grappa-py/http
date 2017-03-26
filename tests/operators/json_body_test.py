import pook
import pytest
import requests


def test_json_operator(should):
    with pook.use():
        pook.get('foo.com', reply=200, response_json={'foo': 'bar'})
        res = requests.get('http://foo.com')

        res | should.have.json.equal.to({'foo': 'bar'})

        with pytest.raises(AssertionError):
            res | should.have.body('foo')


def test_json_complex(should):
    json = {
        'foo': {
            'foo': 123,
            'bar': [
                {'baz': True}
            ]
        },
        'bar': [1, 2, 3],
        'baz': {
            'foo': False
        }
    }

    with pook.use():
        pook.get('foo.com', reply=200, response_json=json)
        res = requests.get('http://foo.com')
        res | should.have.json.equal.to(json)


def test_json_chained_operators(should):
    json = {
        'foo': {
            'foo': 123,
            'bar': [
                {'baz': True}
            ]
        },
        'bar': [1, 2, 3],
        'baz': {
            'foo': False
        }
    }

    with pook.use():
        pook.get('foo.com', reply=200, response_json=json)
        res = requests.get('http://foo.com')
        res | should.have.json.key('foo') > should.be.a('dict')
        res | should.have.json.key('foo').that.should.be.a('dict')
