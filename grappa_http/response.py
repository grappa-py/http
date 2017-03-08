class Response(object):

    def __init__(self, adapter):
        self.adapter = adapter

    @property
    def status(self):
        return self.adapter.status

    @property
    def status_code(self):
        return self.adapter.status_code
