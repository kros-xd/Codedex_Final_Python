'''
We are using packages: 'openai', 'python-dotenv'.
make sure these versions >= 'python-dotenv 0.21.0', 'openai 1.0.0'.

When using this file. PLEASE make sure to use your own API key from OpenAI and place it in a .env file
with the name 'API_KEY'. Otherwise, you will need to make manually adjustments to match your named variables.
'''

import openai
from dotenv import dotenv_values

CONFIG = dotenv_values('.env') # constant variable for enviorement variable housing our api key.
KEY = CONFIG['API_KEY'] # grabs api key as a dictionary and stores it in const 'KEY' variable.

openai.api_key = KEY

def generate_blog(topic):
    
    # 'response' stores the output created by openai.
    response = openai.completions.create(
        model = 'gpt-3.5-turbo-instruct', # 'model' uses a specific model made by openai.
        prompt = 'Write a paragraph about the following topic. ' + topic, # takes in our 'topic' argument passed in and chat will try to follow it's instruction.
        max_tokens = 400, # Tokens -- determines length of paragraph. 75 words is roughly 100 tokens. 1paragrah:400tokens rough ratio.
        temperature = 0.3 # determines the randomness of the response. Can be fine tuned using a range (0, 1). 0 being more direct/clear and 1 being different and more creative.
    )

    output = response.choices[0].text
    return output

def main():
    
    result = generate_blog('python')
    print(result)

if __name__ == '__main__':
    main()