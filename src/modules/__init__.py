__all__ = ['ModuleType']

from enum import Enum, EnumMeta, unique
from src.modules.text_input import TextInput
from src.modules.text import Text
from src.modules.openai import OpenAI


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
