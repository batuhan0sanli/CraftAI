import os

from dotenv import dotenv_values

__all__ = [
    'config',
]


def _get_env(env: str, default=None):
    if env in os.environ:
        return os.environ[env]
    elif env in dotenv_values('.env'):
        return dotenv_values('.env')[env]
    elif default is not None:
        return default
    else:
        raise Exception(f'Environment variable {env} not defined')


class Config:
    OPENAI_API_KEY = _get_env('OPENAI_API_KEY')
    OPENAI_MODEL = _get_env('OPENAI_MODEL', 'gpt-3.5-turbo')
    OPENAI_TEMPERATURE = _get_env('OPENAI_TEMPERATURE', 0)
    OPENAI_MAX_TOKENS = _get_env('OPENAI_MAX_TOKENS', 256)


config = Config()
