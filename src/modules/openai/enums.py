from enum import Enum


class OpenAIRole(Enum):
    system = 'system'
    user = 'user'
    assistant = 'assistant'


class OpenAIEndpoint(Enum):
    chat_completion = 'chat_completion'
