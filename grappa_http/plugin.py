from .operators import get


def register(engine):
    """
    Plugin register function.
    """
    engine.register(*get())
