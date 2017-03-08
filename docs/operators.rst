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
-----------------------  ------------------------
 **Resets context**      no
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

TBD


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
 **Related operators**   headers_
=======================  ========================

**Assertion form**:

.. code-block:: python

    'foo' | should.ends_with('o')
    'foo' | should.ends_with('oo')
    [1, 2, 3] | should.ends_with.number(3)
    iter([1, 2, 3]) | should.ends_with.numbers(2, 3)
    OrderedDict([('foo', 0), ('bar', 1)]) | should.ends_with.item('bar')

.. code-block:: python

    'foo' | expect.to.ends_with('o')
    'foo' | expect.to.ends_with('oo')
    [1, 2, 3] | expect.to.ends_with.number(3)
    iter([1, 2, 3]) | expect.to.ends_with.numbers(2, 3)
    OrderedDict([('foo', 0), ('bar', 1)]) | expect.to.ends_with('bar')

**Negation form**:

.. code-block:: python

    'foo' | should.do_not.ends_with('f')
    'foo' | should.do_not.ends_with('o')
    [1, 2, 3] | should.do_not.ends_with(2)
    iter([1, 2, 3]) | should.do_not.ends_with.numbers(3, 4)
    OrderedDict([('foo', 0), ('bar', 1)]) | should.ends_with('foo')

.. code-block:: python

    'foo' | expect.to_not.ends_with('f')
    'foo' | expect.to_not.ends_with('oo')
    [1, 2, 3] | expect.to_not.ends_with.number(2)
    iter([1, 2, 3]) | expect.to_not.ends_with.numbers(1, 2)
    OrderedDict([('foo', 0), ('bar', 1)]) | expect.to_not.ends_with('foo')
