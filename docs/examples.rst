Examples
========

Basic response assertion
------------------------

.. code-block:: python


    res = requests.get('http://httpbin.org/status/204')
    res | should.be.response.status(204)

    # Or alternatively using the string notation
    res | should.be.response.status('No Content')
