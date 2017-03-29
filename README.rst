.. image:: http://i.imgur.com/kKZPYut.jpg
   :width: 100%
   :alt: grappa logo
   :align: center


|Build Status| |PyPI| |Coverage Status| |Documentation Status| |Stability| |Quality| |Versions| |SayThanks|

About
-----

HTTP request/response assertion plugin for `grappa`_.
``grappa-http`` extends ``grappa`` assertion operators with HTTP protocol testing.

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
    res | should.implement.jsonschema({
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


Full-featured error report example:

.. code-block:: python

    Traceback (most recent call last):
      File "grappa-http/tests/http_test.py", line 38, in test_http_tutorial
        res | should.have.body.equal.to('{\n    "foo": "baa"\n}')
      File "grappa/grappa/test.py", line 208, in __ror__
        return self.__overload__(value)
      File "grappa/grappa/test.py", line 196, in __overload__
        return self.__call__(subject, overload=True)
      File "grappa/grappa/test.py", line 73, in __call__
        return self._trigger() if overload else Test(subject)
      File "grappa/grappa/test.py", line 113, in _trigger
        raise err
    AssertionError: Oops! Something went wrong!

      The following assertion was not satisfied
        subject "{\n    "foo": "bar"\n}" should have body equal to "{\n    "foo": "baa"\n}"

      What we expected
        a response body data equal to:
            {
                "foo": "baa"
            }

      What we got instead
        a response body with data:
            {
                "foo": "bar"
            }

      Difference comparison
        >   {
        > -     "foo": "bar"
        > ?               ^
        > +     "foo": "baa"
        > ?               ^
        >   }

      Where
        File "grappa-http/tests/http_test.py", line 38, in test_http_tutorial

        30|       res | should.have.content('json')
        31|
        32|       # Test response headers
        33|       (res | (should.have.header('Content-Type')
        34|               .that.should.be.equal('application/json')))
        35|       res | should.have.header('Server').that.should.contain('nginx')
        36|
        37|       # Test response body
        38| >     res | should.have.body.equal.to('{\n    "foo": "baa"\n}')
        39|       res | should.have.body.that.contains('foo')
        40|
        41|       # Test response body length
        42|       res | should.have.body.length.of(20)
        43|       res | should.have.body.length.higher.than(10)
        44|
        45|       # Test response JSON body


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

-  ✔  `requests`_
-  ✘  `aiohttp`_ (``work in progress``)

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
.. |SayThanks| image:: https://img.shields.io/badge/Say%20Thanks!-%F0%9F%A6%89-1EAEDB.svg
  :target: https://saythanks.io/to/h2non
  :alt: Say Thanks
