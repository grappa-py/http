import pook
import pytest
import requests


def test_method_presence(should):
    with pook.use():
        pook.get('foo.com', reply=200, response_type='json')

        res = requests.get('http://foo.com')
        res | should.have.method('GET')
        res | should.have.method.equal.to('get')
        res | should.have_not.method.equal.to('POST')

        with pytest.raises(AssertionError):
            res | should.have.method.equal.to('POST')

        with pytest.raises(AssertionError):
            res | should.have_not.method.equal.to('GET')
