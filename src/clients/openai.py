import openai

from src.config import config


class OpenAIClient:
    instance = None

    def __init__(self):
        if not config.OPENAI_API_KEY:
            raise Exception('OPENAI_API_KEY not defined')
        openai.api_key = config.OPENAI_API_KEY

    def __new__(cls):
        if not cls.instance:
            cls.instance = super(OpenAIClient, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def chat_completion(messages):
        completion = openai.ChatCompletion.create(
            model=config.OPENAI_MODEL,
            messages=messages,
            temperature=config.OPENAI_TEMPERATURE,
            max_tokens=config.OPENAI_MAX_TOKENS,
        )
        print("Used token count:", completion.usage.total_tokens)
        return completion.choices[0].message.content
