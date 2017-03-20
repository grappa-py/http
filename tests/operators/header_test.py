import pook
import pytest
import requests


@pook.on
def test_header_presence(should):
    pook.get('foo.com', reply=200, response_type='json')
    res = requests.get('http://foo.com')

    res | should.have.header('Content-Type')
    res | should.not_have.header('Server')

    with pytest.raises(AssertionError):
        res | should.have.header('Server')


@pook.on
def test_header_value(should):
    pook.get('foo.com', reply=200, response_type='json')
    res = requests.get('http://foo.com')

    res | should.have.header('Content-Type', 'application/json')

    (res
        | should.have.header('Content-Type')
        > should.be.equal('application/json'))

    with pytest.raises(AssertionError):
        res | should.have.header('Server', 'foo')

    with pytest.raises(AssertionError):
        res | should.have.header('Server')
