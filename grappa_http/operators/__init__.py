# -*- coding: utf-8 -*-
import functools

# Module symbols to export
__all__ = ('operators', 'get')


# List of built-in operators
operators = (
    # Module name  # Operator class to import
    ('attributes', ),
    ('url',         'UrlOperator'),
    ('body',        'BodyOperator'),
    ('json_body',   'JsonOperator'),
    ('method',      'MethodOperator'),
    ('header',      'HeaderOperator'),
    ('json_schema', 'JsonSchemaOperator'),
    ('content',     'ContentTypeOperator'),
    ('status',      'StatusOperator', 'OkStatusOperator',
                    'ServerErrorStatusOperator', 'BadRequestStatusOperator'),
)


def get():
    """
    Loads the built-in operators into the global test engine.
    """
    def reducer(acc, operator):
        module, symbols = operator[0], operator[1:]
        path = 'grappa_http.operators.{}'.format(module)

        # Dynamically import modules
        operator = __import__(path, None, None, symbols)

        # Register operators in the test engine
        return acc + [getattr(operator, symbol) for symbol in symbols]

    return functools.reduce(reducer, operators, [])
