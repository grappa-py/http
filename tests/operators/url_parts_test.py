import pook
import pytest
import requests


@pook.on
def test_url_protocol_operator(should):
    pook.get('foo.com', reply=200, persist=True, response_type='json')
    requests.get('http://foo.com') | should.have.url.protocol('http')

    # Strict comparison
    # requests.get('http://foo.com') | should.have.url('http://foo.com/')

    with pytest.raises(AssertionError):
        requests.get('http://foo.com') | should.have.url('bar')


@pook.on
def test_url_hostname_operator(should):
    pook.get('foo.com', reply=200, persist=True, response_type='json')

    requests.get('http://foo.com') | should.have.url.hostname('foo.com')
    requests.get('http://foo.com') | should.have.url.hostname('foo',
                                                              strict=False)

    with pytest.raises(AssertionError):
        requests.get('http://foo.com') | should.have.url('bar')


@pook.on
def test_url_port_operator(should):
    pook.get('foo.com', reply=200, persist=True, response_type='json')
    pook.get('https://foo.com', reply=200, persist=True, response_type='json')

    requests.get('http://foo.com') | should.have.url.port(80)
    requests.get('http://foo.com:8080') | should.have.url.port(8080)
    requests.get('https://foo.com') | should.have.url.port(443)

    with pytest.raises(AssertionError):
        requests.get('http://foo.com') | should.have.url('bar')


@pook.on
def test_url_path_operator(should):
    pook.get('foo.com', reply=200, persist=True, response_type='json')
    pook.get('foo.com/bar/baz', reply=200, persist=True, response_type='json')

    requests.get('http://foo.com/') | should.have.url.path('/')
    requests.get('http://foo.com/bar/baz') | should.have.url.path('/bar/baz')
    requests.get('http://foo.com/bar/baz') | should.have.url.path('baz',
                                                                  strict=False)


@pook.on
def test_url_query_operator(should):
    pook.get('foo.com/?x=y&z=w', reply=200, persist=True, response_type='json')

    (requests.get('http://foo.com/?x=y&z=w')
        | should.have.url.query({'x': 'y'})
        | should.have.url.query({'z': ['w']}))

    pook.get('foo.com/?foo=bar', reply=200, persist=True, response_type='json')
    (requests.get('http://foo.com/?foo=bar')
        | should.have.url.query({'foo': True}))

    (requests.get('http://foo.com/?foo=bar')
        | should.have.url.query({'foo': ['a', 'b']}, strict=False))

    with pytest.raises(AssertionError):
        (requests.get('http://foo.com/?foo=bar')
            | should.have.url.query({'bar': 'foo'}))
