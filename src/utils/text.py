class TextObj(object):
    def __init__(self, text: str, variables: dict = None) -> None:
        self.text = text
        self.variables = variables or {}

    def __str__(self) -> str:
        return self.text.format(**self.variables)

    def __repr__(self) -> str:
        return self.__str__()

    def __call__(self, *args, **kwargs):
        return self.__str__()
