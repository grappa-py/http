# -*- coding: utf-8 -*-

# Module symbols to export
__all__ = ('operators', 'get')


# List of built-in operators
operators = (
    # Module name  # Operator class to import
    ('attributes', ),
    ('status',     'StatusOperator'),
)


def get():
    """
    Loads the built-in operators into the global test engine.
    """
    acc = []

    for operator in operators:
        module, symbols = operator[0], operator[1:]
        path = 'grappa_http.operators.{}'.format(module)

        # Dynamically import modules
        operator = __import__(path, None, None, symbols)

        # Register operators in the test engine
        acc += [getattr(operator, symbol) for symbol in symbols]

    return acc
