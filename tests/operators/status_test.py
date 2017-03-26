import pook
import pytest
import requests


def test_status(should):
    with pook.use():
        pook.get('foo.com', reply=201)
        requests.get('http://foo.com') | should.be.status(201)

        pook.get('foo.com', reply=200)
        requests.get('http://foo.com') | should.be.status('OK')

        with pytest.raises(AssertionError):
            pook.get('foo.com', reply=500)
            requests.get('http://foo.com') | should.be.status('OK')


def test_status_ok(should):
    with pook.use():
        pook.get('foo.com', reply=200)
        requests.get('http://foo.com') | should.be.ok

        with pytest.raises(AssertionError):
            pook.get('foo.com', reply=500)
            requests.get('http://foo.com') | should.be.ok


def test_status_bad(should):
    with pook.use():
        pook.get('foo.com', reply=403)
        requests.get('http://foo.com') | should.be.bad_request

        with pytest.raises(AssertionError):
            pook.get('foo.com', reply=204)
            requests.get('http://foo.com') | should.be.bad_request


def test_status_error(should):
    with pook.use():
        pook.get('foo.com', reply=500)
        requests.get('http://foo.com') | should.be.server_error

        with pytest.raises(AssertionError):
            pook.get('foo.com', reply=404)
            requests.get('http://foo.com') | should.be.server_error
