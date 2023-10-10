import os
import toml
from configparser import ConfigParser

__all__ = [
    'config',
]

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(ROOT_DIR, 'config.toml')

config = ConfigParser()
config.read(CONFIG_PATH)

config['openai']['api_key'] = config['openai']['api_key'].replace("'", '')

# config = toml.load(CONFIG_PATH)
