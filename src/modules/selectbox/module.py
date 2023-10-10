from src.base.base_module import BaseModule
from .schema import ModuleSchema
from src.utils import TextObj


class SelectBox(BaseModule):
    schema = ModuleSchema

    def build_method(self) -> None:
        label = TextObj(self.data['label'], self.variables)()
        options = [TextObj(option, self.variables)() for option in self.data['options']]
        return self.container.selectbox(label, options)
