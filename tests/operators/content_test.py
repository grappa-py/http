import pook
import pytest
import requests


def test_content_operator(should):
    with pook.use():
        pook.get('foo.com', reply=200, response_type='json')
        requests.get('http://foo.com') | should.have.content('json')

        pook.get('foo.com', reply=200, response_type='xml')
        requests.get('http://foo.com') | should.have.content('xml')

        pook.get('foo.com', reply=200, response_type='html')
        requests.get('http://foo.com') | should.have.content('html')

        (pook.get('foo.com')
            .reply(200)
            .set('Content-Type', 'application/json; encoding=utf-8'))
        requests.get('http://foo.com') | should.have.content('json')

        (pook.get('foo.com')
            .reply(200)
            .set('Content-Type', 'application/json; encoding=utf-8'))
        (requests.get('http://foo.com')
            | should.have.content('application/json; encoding=utf-8'))

        with pytest.raises(AssertionError):
            pook.get('foo.com', reply=500)
            requests.get('http://foo.com') | should.have.content('json')
