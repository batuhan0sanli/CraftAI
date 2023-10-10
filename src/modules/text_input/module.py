from src.base.base_module import BaseModule
from .schema import TextInputSchema
from src.utils import TextObj


class TextInput(BaseModule):
    schema = TextInputSchema

    def build_method(self) -> None:
        label = TextObj(self.data['label'], self.variables)()
        placeholder = TextObj(self.data['placeholder'], self.variables)()
        return self.container.text_input(label=label, value=placeholder)
