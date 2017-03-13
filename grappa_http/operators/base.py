from grappa import Operator
from .. import adapters


class BaseOperator(Operator):
    """
    Implements the HTTTP base operator.
    """

    def match(self, response, *expected, **kw):
        # If response was already processed as adapter
        if isinstance(response, adapters.BaseAdapter):
            return self._match(response, *expected, **kw)

        # Match HTTP client adapter based on the response object
        adapter = adapters.match(response)

        # Validate supported HTTP client adapter
        if not adapter:
            return False, [
                'subject is not a supported HTTP response object: {}'.format(
                    response
                )
            ]

        # Assign response
        self.subject = adapter(response)

        # Trigger match operator method
        return self._match(self.subject, *expected, **kw)
