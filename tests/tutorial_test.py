import pook
import requests
from grappa_http import should


def test_http_tutorial():
    # Activate the HTTP mock engine
    pook.on()

    # Register a sample mock
    pook.get('server.org/foo?bar=baz', reply=200,
             response_headers={'Server': 'nginx'},
             response_json={'foo': 'bar'})

    # Perform HTTP request
    res = requests.get('http://server.org/foo?bar=baz')

    # Test response status to be OK
    res | should.be.ok
    # Or alternatively using the status code
    res | should.have.status(200)

    # Test request URL
    res | should.have.url.hostname('server.org')
    res | should.have.url.port(80)
    res | should.have.url.path('/foo')
    res | should.have.url.query.params({'bar': 'baz'})

    # Test response body MIME content type
    res | should.have.content('json')

    # Test response headers
    (res | (should.have.header('Content-Type')
            .that.should.be.equal('application/json')))
    res | should.have.header('Server').that.should.contain('nginx')

    # Test response body
    res | should.have.body.equal.to('{\n    "foo": "bar"\n}')
    res | should.have.body.that.contains('foo')

    # Test response body length
    res | should.have.body.length.of(20)
    res | should.have.body.length.higher.than(10)

    # Test response JSON body
    res | should.have.json.equal.to({'foo': 'bar'})
    res | should.have.json.have.key('foo') > should.be.equal.to('bar')

    # Validate response JSON bodies using JSONSchema
    res | should.have.jsonschema({
        '$schema': 'http://json-schema.org/draft-04/schema#',
        'title': 'Response JSON',
        'type': 'object',
        'required': ['foo'],
        'properties': {
            'foo': {
                'description': 'foo always means foo',
                'type': 'string'
            }
        }
    })
