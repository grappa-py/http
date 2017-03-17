import pook
import pytest
import requests


def test_body_operator(should):
    pook.get('foo.com', reply=200, response_body='hello world')
    res = requests.get('http://foo.com')

    res | should.have.body.equal.to('hello world')

    with pytest.raises(AssertionError):
        res | should.have.body('foo')


def test_json_operator(should):
    pook.get('foo.com', reply=200, response_json={'foo': 'bar'})
    res = requests.get('http://foo.com')

    res | should.have.json.equal.to({'foo': 'bar'})

    with pytest.raises(AssertionError):
        res | should.have.body('foo')
