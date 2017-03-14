from .operators import get

# Stores if the plugin has been registered
registered = False


def register(engine):
    """
    Plugin register function.
    """
    global registered
    if registered:
        return

    registered = True
    engine.register(*get())
