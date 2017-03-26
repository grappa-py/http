import pook
import pytest
import requests


def test_body_operator(should):
    with pook.use():
        pook.get('foo.com', reply=200, response_body='hello world')
        res = requests.get('http://foo.com')

        res | should.have.body.equal.to('hello world')

        with pytest.raises(AssertionError):
            res | should.have.body('foo')


def test_body_match(should):
    with pook.use():
        pook.get('foo.com', reply=200, response_body='hello world')
        res = requests.get('http://foo.com')

        res | should.have.body.to.match(r'(\w+) world$')
        res | should.have.body('hello world')

        pook.get('foo.com', reply=200, response_json={'foo': 'bar'})
        res = requests.get('http://foo.com')
        res | should.have.body.json({'foo': 'bar'})


def test_body_length(should):
    with pook.use():
        pook.get('foo.com', reply=200, response_body='hello world')
        res = requests.get('http://foo.com')

        res | should.have.body.length(11)
        res | should.have.body.length.higher.than(10)
