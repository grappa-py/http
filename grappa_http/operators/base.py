from grappa import Operator
from .. import adapters


class BaseOperator(Operator):
    """
    Implements the HTTTP base operator.
    """

    def isadapter(self, response):
        return isinstance(response, adapters.BaseAdapter)

    def adapt(self, response):
        # If response was already processed as adapter
        if self.isadapter(response):
            return response

        # Match HTTP client adapter based on the response object
        adapter = adapters.match(response)
        if not adapter:
            return

        # Return wrapper response adapter
        return adapter(response)

    def on_access(self, response):
        """
        On access matcher operator event subscriber
        """
        ismatcher = self.kind == Operator.Type.MATCHER
        if not ismatcher or not hasattr(self, '_on_access'):
            return

        try:
            res = self.adapt(response)
        except:
            res = response

        self._on_access(res)

        # Set original subject reference
        self.ctx.original_subject = response

    def match(self, response, *expected, **kw):
        # Adapt response object based on the HTTP client
        if not self.ctx.original_subject:
            response = self.adapt(response)

            # Validate supported HTTP client adapter
            if not response:
                return False, [
                    'subject is not a supported HTTP '
                    'response object: {}'.format(response)
                ]

        # Assign response
        self.subject = response

        # Trigger match operator method
        return self._match(self.subject, *expected, **kw)
