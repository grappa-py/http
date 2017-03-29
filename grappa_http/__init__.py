# -*- coding: utf-8 -*
"""
`grappa_http`

Usage
-----

    import grappa
    import grappa_http

    # Register plugin
    grappa.use(grappa_http)

    # Use plugin assertion
    res = requests.get('httpbin.org/status/204')
    res | should.have.status(204)


For assertion operators and aliases, see `operators documentation`_.

.. _`operators documentation`: operators.html

Reference
---------
"""
# Export register function
from .plugin import register
from grappa import should, expect, use

# Register Python operator
__all__ = ('should', 'expect', 'register')

# Package metadata
__author__ = 'Tomas Aparicio'
__license__ = 'MIT'

# Current package version
__version__ = '0.1.1'

# Self-register plugin in grappa
use(register)
