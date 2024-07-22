'''
We are using modules: 'openai', 'python-dotenv'.
make sure these versions >= 'python-dotenv 0.21.0', 'openai 1.0.0'.

When using this file. PLEASE make sure to use your own API key from OpenAI and place it in a .env file
with the name 'API_KEY'. Otherwise, you will need to make manually adjustments to match your named variables.
'''

import openai
from dotenv import dotenv_values

CONFIG = dotenv_values('.env') # constant variable for enviorement variable housing our api key.
KEY = CONFIG['API_KEY'] # grabs api key as a dictionary and stores it in const 'KEY' variable.
