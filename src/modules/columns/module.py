from streamlit import columns
from src.base.base_module import BaseModule
from .schema import ModuleSchema
import src.builders as builders


class Columns(BaseModule):
    schema = ModuleSchema

    def build_method(self) -> None:
        if len(self.data['modules']) != self.data['spec']:
            raise Exception('Spec and modules length must be equal')
        col_list = columns(self.data['spec'])
        for col, module in zip(col_list, self.data['modules']):
            builders.ModuleBuilder(module, self.variables, col).build()
