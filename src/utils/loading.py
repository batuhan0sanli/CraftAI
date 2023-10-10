import contextlib

from streamlit import spinner


@contextlib.contextmanager
def loading(variables, response_text=None, text: str = "In progress..."):
    """Temporarily displays a message while executing a block of code.

    Parameters
    ----------
    text : str
        A message to display while executing that block

    Example
    -------

    >>> from src.utils import loading
    >>> from time import sleep
    >>>
    >>> with loading(variables, response_text):
    >>>     sleep(5)
    :param response_text:
    :param text:
    :param variables:

    """
    with spinner(text):
        # todo: add loading to variables
        # if response_text:
        #     variables.set(response_text, 'Loading')
        yield
