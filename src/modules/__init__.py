__all__ = ['ModuleType']

from enum import Enum, EnumMeta, unique

from src.modules.openai import OpenAI
from src.modules.text import Text
from src.modules.text_area_input import TextAreaInput
from src.modules.text_input import TextInput


class EnumMetaAssert(EnumMeta):
    def __getitem__(self, name):
        try:
            return super().__getitem__(name)
        except (TypeError, KeyError) as error:
            raise Exception(f'Module "{name}" not found') from error


@unique
class ModuleType(Enum, metaclass=EnumMetaAssert):
    text_input = TextInput
    text = Text
    openai = OpenAI
    text_area_input = TextAreaInput
