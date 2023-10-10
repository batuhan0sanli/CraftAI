from src.modules import ModuleType
from src.variables import Variables


class ModuleBuilder:
    def __init__(self, raw_data: dict, variables: Variables, container):
        self.raw_data = raw_data
        self.variables = variables
        self.container = container

    def control(self):
        if 'module' not in self.raw_data:
            raise Exception('Module type not specified')

    def build(self):
        self.control()
        module = self.raw_data.pop('module')
        print("Building module", module)  # todo: convert to logger
        module_type = ModuleType.__getitem__(module)
        module_type.value(self.raw_data, self.variables, self.container).build()
