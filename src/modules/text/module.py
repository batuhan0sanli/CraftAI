from streamlit import write

from src.base.base_module import BaseModule
from src.utils import TextObj
from .schema import ModuleSchema


class Text(BaseModule):
    schema = ModuleSchema

    def build_method(self) -> None:
        text = TextObj(self.data['text'], self.variables)()
        write(text)
