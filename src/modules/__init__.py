__all__ = ['ModuleType']

from enum import Enum
from src.modules.text_input import TextInput
from src.modules.text import Text


class ModuleType(Enum):
    text_input = TextInput
    text = Text
    # openai = 'openai'
