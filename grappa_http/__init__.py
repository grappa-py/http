# -*- coding: utf-8 -*
"""
`grappa_http` provides HTTP protocol assertion for `grappa` testing library.

Example::

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
from . import adapters
from .plugin import register
from grappa import should, expect, use

# Register Python operator
__all__ = ('should', 'expect', 'register', 'adapters')

# Package metadata
__author__ = 'Tomas Aparicio'
__license__ = 'MIT'

# Current package version
__version__ = '0.1.2'

# Self-register plugin in grappa
use(register)
