'''
We are using modules: 'openai', 'python-dotenv', 'os'.
make sure these versions >= 'python-dotenv 0.21.0', 'openai 1.0.0'.

When using this file. PLEASE make sure to use your own API key from OpenAI and place it in a .env file
with the name 'API_KEY'. Otherwise, you will need to make adjustments to match your named variables.
'''

import openai
from dotenv import dotenv_values
import os # this is only used to clear the terminal screen.

CONFIG = dotenv_values('.env') # constant variable for enviorement variable housing our api key.
KEY = CONFIG['API_KEY'] # grabs api key as a dictionary and stores it in const 'KEY' variable.

openai.api_key = KEY # Authorizes our API key!

def clear_screen():
    # check if user OS is on windows
    if os.name == 'nt':
        os.system('cls')
    # If it's not windows, it must be mac, linux, or something else.
    else:
        os.system('clear')


def generate_blog(topic):
    # 'response' stores the output created by openai.
    response = openai.completions.create(
        model = 'gpt-3.5-turbo-instruct', # 'model' uses a specific model made by openai.
        prompt = 'Write a paragraph about the following topic. ' + topic, # takes in our 'topic' argument passed in and GPT-3.5 will try to follow it's instruction.
        max_tokens = 400, # Tokens -- determines length of paragraph. 75 words is roughly 100 tokens. 1paragrah:400tokens rough ratio.
        temperature = 0.375 # determines the randomness of the response. Can be fine tuned using a range (0, 1). 0 being more direct/clear and 1 being different each time and more creative.
    )

    output = response.choices[0].text
    return output


def user_input():
    # Made function to grab user input.
    try:
        prompt = input("\n\tEnter: ")
        return prompt
    
    except Exception as e:
        print(f"\n{e}! Something went wrong.")


def main():

    running = True
    while running:

        clear_screen() # clears terminal screen
        print("\nWould you like to generate a paragraph based on a given topic?")
        print("\n\t1.) Yes\n\t2.) No")
        # grab user choice if they want to generate a paragraph.
        choice = user_input() 
        # choice options to check in conditional while loop.
        options = [
            'yes',
            'y',
            '1',
            'no',
            'n',
            '2'
        ]
        
        while choice.lower() not in options: # check to see if the given choice is valid.
            
            clear_screen() # clears terminal screen
            print(f"\n'{choice}' Is not a valid option. Please type the corresponding number or choice.")
            print("\n\nWould you like to generate a paragraph based on a given topic?")
            print("\n\t1.) Yes\n\t2.) No")
            choice = user_input()

        while choice in options[:3]: # keep looping as long as the user choice is in first 3 items of options list.
            
            clear_screen()
            print("\nWhat would you like the topic to be about?")
            prompt = user_input()
            print('\n'*4)
            print(generate_blog(prompt))
            print('\n'*4)
            print("\nWould you like to write about another topic?")
            choice = user_input()

        clear_screen()
        print("\nThanks for trying this out!")
        running = False

if __name__ == '__main__':
    main()