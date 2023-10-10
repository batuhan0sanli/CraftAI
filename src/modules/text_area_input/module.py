from src.base.base_module import BaseModule
from .schema import ModuleSchema
from src.utils import TextObj


class TextAreaInput(BaseModule):
    schema = ModuleSchema

    def build_method(self) -> None:
        label = TextObj(self.data['label'], self.variables)()
        placeholder = TextObj(self.data['placeholder'], self.variables)()
        return self.container.text_area(label=label, value=placeholder)
