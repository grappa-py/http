.. image:: http://i.imgur.com/kKZPYut.jpg
   :width: 100%
   :alt: grappa logo
   :align: center


|Build Status| |PyPI| |Coverage Status| |Documentation Status| |Stability| |Quality| |Versions|

About
-----

HTTP request/response assertion plugin for `grappa`_.

To get started, take a look to the `documentation`_, `tutorial`_ and `examples`_.

Status
------

``grappa-http`` is still **beta quality** software.

Showcase
--------

.. code-block:: python

    import pook
    import requests
    from grappa_http import should

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

Features
--------

-  Full-featured HTTP response assertions.
-  Supports any protocol primitive assertions.
-  First-class support for JSON body assertion.
-  Built-in JSONSchema validation.
-  Full-features request URL validation.
-  Featured regular expression based assertion.
-  Works with ``requests`` and ``aiohttp`` HTTP clients.
-  Friendly and detailed assertion error reporting with body diff comparisons.
-  Provides both ``expect`` and ``should`` assertion styles.
-  Testing framework agnostic. Works with ``unittest``, ``nosetests``, ``pytest``, ``behave``...
-  Works with Python 2.6+, 3+, PyPy and possibly other Python implementations.

Supported HTTP clients
----------------------

-  [x] `requests`_
-  [_] `aiohttp`_ (``work in progress``)

Installation
------------

Using ``pip`` package manager:

.. code-block:: bash

    pip install --upgrade grappa-http

Or install the latest sources from Github:

.. code-block:: bash

    pip install -e git+git://github.com/grappa-py/http.git#egg=grappa


.. _Python: http://python.org
.. _`grappa`: https://grappa.readthedocs.io
.. _`documentation`: http://grappa-http.readthedocs.io
.. _`tutorial`: http://grappa-http.readthedocs.io/en/latest/tutorial.html
.. _`examples`: http://grappa-http.readthedocs.io/en/latest/examples.html
.. _`requests`: http://docs.python-requests.org/en/master/
.. _`aiohttp`: http://aiohttp.readthedocs.io/en/stable/

.. |Build Status| image:: https://travis-ci.org/grappa-py/http.svg?branch=master
   :target: https://travis-ci.org/grappa-py/http
.. |PyPI| image:: https://img.shields.io/pypi/v/grappa-http.svg?maxAge=2592000?style=flat-square
   :target: https://pypi.python.org/pypi/grappa-http
.. |Coverage Status| image:: https://coveralls.io/repos/github/grappa-py/http/badge.svg?branch=master
   :target: https://coveralls.io/github/grappa-py/http?branch=master
.. |Documentation Status| image:: https://readthedocs.org/projects/grappa-http/badge/?version=latest
   :target: http://grappa-http.readthedocs.io/en/latest/?badge=latest
.. |Quality| image:: https://codeclimate.com/github/grappa-py/http/badges/gpa.svg
   :target: https://codeclimate.com/github/grappa-py/http
   :alt: Code Climate
.. |Stability| image:: https://img.shields.io/pypi/status/grappa-http.svg
   :target: https://pypi.python.org/pypi/grappa-http
   :alt: Stability
.. |Versions| image:: https://img.shields.io/pypi/pyversions/grappa-http.svg
   :target: https://pypi.python.org/pypi/grappa-http
   :alt: Python Versions
