from src.config import config
import openai
from typing import List


class OpenAIClient:
    instance = None

    def __init__(self):
        openai.api_key = config['openai']['api_key']

    def __new__(cls):
        if not cls.instance:
            cls.instance = super(OpenAIClient, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def chat_completion(messages):
        completion = openai.ChatCompletion.create(
            model=config['openai'].get('model', 'gpt-3.5-turbo'),
            messages=messages,
            temperature=config['openai'].get('temperature', 0),
            max_tokens=config['openai'].get('max_tokens', 256),
        )
        return completion.choices[0].message.content
