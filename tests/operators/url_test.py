import pook
import pytest
import requests


@pook.on
def test_url_operator(should):
    pook.get('foo.com', reply=200, persist=True, response_type='json')
    requests.get('http://foo.com') | should.have.url('http://foo.com')

    res = requests.get('http://foo.com')
    res | should.have.url('foo.com')
    res | should.have.url.equal.to('http://foo.com')
    res | should.have.url.that.contains('foo.com')
    res | should.have.url.that.matches('foo.com/$')

    # Strict comparison
    res | should.have.url('http://foo.com/', strict=True)

    with pytest.raises(AssertionError):
        requests.get('http://foo.com') | should.have.url('bar')

    with pytest.raises(AssertionError):
        (requests.get('http://foo.com')
            | should.have.url('//foo.com', strict=True))
