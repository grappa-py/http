import pook
import pytest
import requests


def test_method_presence(should):
    pook.get('foo.com', reply=200, response_type='json')
    res = requests.get('http://foo.com')

    res | should.have.method('GET')
    res | should.have.method.equal.to('GET')
    res | should.have_not.method.equal.to('POST')

    with pytest.raises(AssertionError):
        res | should.have.method.equal.to('POST')

    with pytest.raises(AssertionError):
        res | should.have_not.method.equal.to('GET')
