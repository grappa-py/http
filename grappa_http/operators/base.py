from grappa import Operator
from .. import adapters


class BaseOperator(Operator):
    """
    Implements a base operator.
    """

    def match(self, response, *expected, **kw):
        adapter = adapters.match(response)
        if not adapter:
            return False, [
                'unsupported response object: {}'.format(response)]

        res = adapter(response)
        return self._match(res, *expected, **kw)
