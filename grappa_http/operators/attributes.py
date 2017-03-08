# -*- coding: utf-8 -*-
from grappa import attribute


@attribute(operators=('request'))
def response(ctx):
    """
    Semantic attributes providing chainable declarative DSL
    for assertions.
    """
    ctx.negate = False
