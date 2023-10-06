from streamlit import write

from src.base.base_module import BaseModule
from .schema import ModuleSchema


class Text(BaseModule):
    schema = ModuleSchema

    def build(self) -> None:
        write(self.data['text'].format(**self.variables))
