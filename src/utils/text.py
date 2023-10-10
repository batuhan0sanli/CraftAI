from enum import Enum


class TextObj(object):
    def __init__(self, text: str, variables: dict = None) -> None:
        self.text = text
        self.variables = variables or {}

    def __str__(self) -> str:
        # Parse Enum values
        if isinstance(self.text, Enum):
            return self.text.value
        # Parse variables
        return self.text.format(**self.variables)

    def __repr__(self) -> str:
        return self.__str__()

    def __call__(self, *args, **kwargs):
        return self.__str__()
