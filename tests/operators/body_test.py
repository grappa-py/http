import pook
import pytest
import requests


@pook.on
def test_body_operator(should):
    pook.get('foo.com', reply=200, response_body='hello world')
    res = requests.get('http://foo.com')

    res | should.have.body.equal.to('hello world')

    with pytest.raises(AssertionError):
        res | should.have.body('foo')


@pook.on
def test_body_match(should):
    pook.get('foo.com', reply=200, response_body='hello world')
    res = requests.get('http://foo.com')

    res | should.have.body.to.match(r'(\w+) world$')
    res | should.have.body('hello world')

    pook.get('foo.com', reply=200, response_json={'foo': 'bar'})
    res = requests.get('http://foo.com')
    res | should.have.body.json({'foo': 'bar'})
