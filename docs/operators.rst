Assertion Operators
===================

Attributes
----------

response
^^^^^^^^

Response semantic operator for better expressivity

=======================  ========================
 **Type**                attribute
-----------------------  ------------------------
 **Assertion mode**      positive
=======================  ========================

**Examples**:

.. code-block:: python

    response | should.have.response.status(200)
    response | should.have.response.type.of('json')

.. code-block:: python

    response | expect.to.have.response.status(200)
    response | expect.to.have.response.type.of('json')

Accessors
---------

ok
^^

Asserts HTTP response status should be ``200``.

=======================  ========================
 **Type**                attribute
-----------------------  ------------------------
 **Related operators**   server_error_ bad_request_ status_
=======================  ========================

**Assertion form**:

.. code-block:: python

    res | should.be.ok

.. code-block:: python

    res | expect.to.be.ok

**Negation form**:

.. code-block:: python

    res | should.not_be.ok

.. code-block:: python

    res | expect.to_not.be.ok

bad_request
^^^^^^^^^^^

Asserts HTTP response status should be a server error (``400``-``499``).

=======================  ========================
 **Type**                attribute
-----------------------  ------------------------
 **Related operators**   server_error_ ok_ status_
=======================  ========================

**Assertion form**:

.. code-block:: python

    res | should.be.bad_request

.. code-block:: python

    res | expect.to.be.bad_request

**Negation form**:

.. code-block:: python

    res | should.not_be.bad_request

.. code-block:: python

    res | expect.to_not.be.bad_request

server_error
^^^^^^^^^^^^

Asserts HTTP response status should be a server error (``500``-``599``).

=======================  ========================
 **Type**                attribute
-----------------------  ------------------------
 **Related operators**   status_ bad_request_ ok_
=======================  ========================

**Assertion form**:

.. code-block:: python

    res | should.be.server_error

.. code-block:: python

    res | expect.to.be.server_error

**Negation form**:

.. code-block:: python

    res | should.not_be.server_error

.. code-block:: python

    res | expect.to_not.be.server_error

Matchers
--------

status
^^^^^^

Asserts HTTP response status name or code.

=======================  ========================
 **Type**                matcher
-----------------------  ------------------------
 **Chained aliases**     ``code``
-----------------------  ------------------------
 **Related operators**   headers_ bad_request_ ok_ server_error_
=======================  ========================

**Assertion form**:

.. code-block:: python

    res | should.be.status(200)

.. code-block:: python

    res | expect.to.be.status(200)

**Negation form**:

.. code-block:: python

    res | should.not_be.status(200)

.. code-block:: python

    res | expect.to_not.be.status(200)

header
^^^^^^

headers
^^^^^^^

Asserts HTTP response header(s) presence and/or values.

=======================  ========================
 **Type**                matcher
-----------------------  ------------------------
 **Chained aliases**     ``equal`` ``to`` ``be`` ``of``
-----------------------  ------------------------
 **Yields**              ``header value``
-----------------------  ------------------------
 **Related operators**   content_ status_
-----------------------  ------------------------
 **Optional keywords**   ``includes: bool``
=======================  ========================

**Assertion form**:

.. code-block:: python

    res | should.have.header('Content-Type', 'application/json')
    res | should.have.header('Content-Type').equal.to('application/json')

.. code-block:: python

    res | expect.to_not.have.header('Server', 'nginx')
    res | expect.to_not.have.header('server').equal.to('nginx')

**Negation form**:

.. code-block:: python

    res | should.not_have.header('Server', 'nginx')
    res | should.not_have.header('Server').equal.to('nginx')

.. code-block:: python

    res | expect.to.have.header('Server', 'nginx')
    res | expect.to.have.header('server').equal.to('nginx')

ctype
^^^^^

content
^^^^^^^

Asserts HTTP response content type value.

=======================  ========================
 **Type**                matcher
-----------------------  ------------------------
 **Chained aliases**     ``equal`` ``to`` ``be`` ``of`` ``type``
-----------------------  ------------------------
 **Related operators**   header_
=======================  ========================

**Assertion form**:

.. code-block:: python

    res | should.be.content('json')
    res | should.be.content.of('xml')
    res | should.have.response.content.type('html')
    res | should.have.response.content.type('application/json')
    res | should.have.response.content.equal.to('application/json')

.. code-block:: python

    res | expect.to.have.content('json')
    res | expect.to.have.content.of('xml')
    res | expect.to.have.content.type('html')
    res | expect.to.have.response.content.equal.to('application/json')

**Negation form**:

.. code-block:: python

    res | should.not_have.content('json')
    res | should.not_have.content.of('json')

.. code-block:: python

    res | expect.to.not_have.content('json')
    res | expect.to.not_have.content.of('xml')
    res | expect.to.not_have.content.type('html')
    res | expect.to_not.have.response.content.equal.to('application/json')


body
^^^^

data
^^^^

Asserts HTTP response body content as string.

=======================  ========================
 **Type**                matcher
-----------------------  ------------------------
 **Chained aliases**     ``equal`` ``to`` ``be``
-----------------------  ------------------------
 **Yields**              ``body``
-----------------------  ------------------------
 **Related operators**   header_ status_ json_
=======================  ========================

**Assertion form**:

.. code-block:: python

    res | should.have.body('hello world')
    res | should.have.body.equal.to('hello world')
    res | should.have.body.match.to(r'(\w+) world$')
    res | should.have.body.to.contain('world')

.. code-block:: python

    res | expect.to.have.body('hello world')
    res | expect.to.have.body.equal.to('hello world')
    res | expect.to.have.body.to.match(r'(\w+) world$')
    res | expect.to.have.body.to.contain('world')

**Negation form**:

.. code-block:: python

    res | should.not_have.body('hello world')
    res | should.not_have.body.equal.to('hello world')
    res | should.have.body.match.to(r'(\w+) world$')
    res | should.not_have.body.to.contain('world')

.. code-block:: python

    res | expect.to_not.have.body('hello world')
    res | expect.to_not.have.body.equal.to('hello world')
    res | expect.to_not.have.body.to.match(r'(\w+) world$')
    res | expect.to_not.have.body.to.contain('world')


json
^^^^

Asserts HTTP response body JSON content.

=======================  ========================
 **Type**                matcher
-----------------------  ------------------------
 **Chained aliases**     ``equal`` ``to`` ``be``
-----------------------  ------------------------
 **Yields**              ``parsed json``
-----------------------  ------------------------
 **Related operators**   header_ status_ body_ jsonschema_
=======================  ========================

**Assertion form**:

.. code-block:: python

    res | should.have.json({'foo': 'bar'})
    res | should.have.json.equal.to({'foo': 'bar'})
    res | should.have.json(r'(\w+) world$')
    res | should.have.json.to.contain('world')

.. code-block:: python

    res | expect.to.have.json({'foo': 'bar'})
    res | expect.to.have.json.equal.to({'foo': 'bar'})
    res | expect.to.have.json.to.match(r'(\w+) world$')
    res | expect.to.have.json.to.contain('world')

**Negation form**:

.. code-block:: python

    res | should.not_have.json({'foo': 'bar'})
    res | should.not_have.json.equal.to({'foo': 'bar'})
    res | should.have.json.match.to(r'(\w+) world$')
    res | should.not_have.json.to.contain('world')

.. code-block:: python

    res | expect.to_not.have.json({'foo': 'bar'})
    res | expect.to_not.have.json.equal.to({'foo': 'bar'})
    res | expect.to_not.have.json.to.match(r'(\w+) world$')
    res | expect.to_not.have.json.to.contain('world')


jsonschema
^^^^^^^^^^

json_schema
^^^^^^^^^^^

Asserts HTTP response body JSON against a JSONSchema.

=======================  ========================
 **Type**                matcher
-----------------------  ------------------------
 **Chained aliases**     ``equal`` ``to`` ``be`` ``match``
-----------------------  ------------------------
 **Yields**              ``parsed json``
-----------------------  ------------------------
 **Related operators**   header_ body_ json_
=======================  ========================

**Assertion form**:

.. code-block:: python

    res | should.satisfy.jsonschema(schema)
    res | should.satisfy.jsonschema.equal.to(schema)

.. code-block:: python

    res | expect.to.satisfy.jsonschema(schema)
    res | expect.to.satisfy.jsonschema.equal.to(schema)

**Negation form**:

.. code-block:: python

    res | should.do_not.satisfy.jsonschema(schema)
    res | should.do_not.satisfy.jsonschema.equal.to(schema)

.. code-block:: python

    res | expect.to_not.satisfy.jsonschema(schema)
    res | expect.to_not.satisfy.jsonschema.equal.to(schema)

verb
^^^^

method
^^^^^^

Asserts HTTP request method.

=======================  ========================
 **Type**                matcher
-----------------------  ------------------------
 **Chained aliases**     ``equal`` ``to`` ``be``
-----------------------  ------------------------
 **Related operators**   header_ status_ body_
=======================  ========================

**Assertion form**:

.. code-block:: python

    res | should.be.method('GET')

.. code-block:: python

    res | expect.to.be.method('GET')

**Negation form**:

.. code-block:: python

    res | should.not_be.method('GET')

.. code-block:: python

    res | expect.to_not.be.method('GET')

url
^^^

Asserts HTTP request target URL.

=======================  ========================
 **Type**                matcher
-----------------------  ------------------------
 **Chained aliases**     ``equal`` ``to`` ``be``
-----------------------  ------------------------
 **Yields subject**      ``url value``
-----------------------  ------------------------
 **Suboperators**        ``path`` ``port`` ``hostname`` ``query``
-----------------------  ------------------------
 **Related operators**   header_ status_ body_
=======================  ========================

**Assertion form**:

.. code-block:: python

    res | should.have.url('http://foo.org')
    res | should.have.url('foo.org', strict=False)
    res | should.have.url.hostname('foo.org')
    res | should.have.url.port(80)
    res | should.have.url.protocol('http')
    res | should.have.url.path('/bar/baz')
    res | should.have.url.query({'x': 'y', 'z': True})

.. code-block:: python

    res | expect.to.have.url('http://foo.org')
    res | expect.to.have.url('foo.org', strict=False)
    res | expect.to.have.url.hostname('foo.org')
    res | expect.to.have.url.port(80)
    res | expect.to.have.url.protocol('http')
    res | expect.to.have.url.path('/bar/baz')
    res | expect.to.have.url.query({'x': 'y', 'z': True})

**Negation form**:

.. code-block:: python

    res | should.not_have.url('http://foo.org')
    res | should.not_have.url('foo.org', strict=False)
    res | should.not_have.url.hostname('foo.org')
    res | should.not_have.url.port(80)
    res | should.not_have.url.protocol('http')
    res | should.not_have.url.path('/bar/baz')
    res | should.not_have.url.query({'x': 'y', 'z': True})

.. code-block:: python

    res | expect.to_not.have.url('http://foo.org')
    res | expect.to_not.have.url('foo.org', strict=False)
    res | expect.to_not.have.url.hostname('foo.org')
    res | expect.to_not.have.url.port(80)
    res | expect.to_not.have.url.protocol('http')
    res | expect.to_not.have.url.path('/bar/baz')
    res | expect.to_not.have.url.query({'x': 'y', 'z': True})
