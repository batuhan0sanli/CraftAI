from streamlit import text_input

from src.base.base_module import BaseModule
from .schema import TextInputSchema


class TextInput(BaseModule):
    schema = TextInputSchema

    def build(self) -> None:
        res = text_input(label=self.data['label'], value=self.data['placeholder'])
        self.variables.set(self.data['var'], res)
