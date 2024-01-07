import requests
from InquirerPy import prompt
from pprint import pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv
from twilio.rest import Client

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

API_USERNAME = os.environ.get('DEHASHED_USERNAME')
API_KEY = os.environ.get("DEHASHED_API_KEY")

class Dehashed:
    def modules():
        questions = [
                    {
                        'type': 'list',
                        'name': 'choices',
                        'message': 'Please choose query type -',
                        'choices': ['Email', 'Phone', 'Username', 'Address'],
                        'filter': lambda val: val.lower()
                    }
                ]
        answers = prompt(questions)
        
        return answers['choices']
    
    def email(self):
        questions = [
            {
                'type': 'input',
                'name': 'email',
                'message': 'Enter email to lookup...',
            }
        ]

        answers = prompt(questions)
        headers = {
            'Accept': 'application/json',
        }

        response = requests.get(
            'https://api.dehashed.com/search?query=email:' + answers['email'],
            headers=headers,
            auth=(API_USERNAME, API_KEY),
        )
        print(response.json())
        
    def phone(self):
        questions = [
            {
                'type': 'input',
                'name': 'phone',
                'message': 'Enter phone number to lookup...',
            }
        ]

        answers = prompt(questions)
        headers = {
            'Accept': 'application/json',
        }

        response = requests.get(
            'https://api.dehashed.com/search?query=phone:' + answers['phone'],
            headers=headers,
            auth=(API_USERNAME, API_KEY),
        )
        print(response.json())
        
    def username(self):
        questions = [
            {
                'type': 'input',
                'name': 'username',
                'message': 'Enter username to lookup...',
            }
        ]

        answers = prompt(questions)
        headers = {
            'Accept': 'application/json',
        }

        response = requests.get(
            'https://api.dehashed.com/search?query=username:' + answers['username'],
            headers=headers,
            auth=(API_USERNAME, API_KEY),
        )
        print(response.json())
        
    def address(self):
        questions = [
            {
                'type': 'input',
                'name': 'address',
                'message': 'Enter address to lookup...',
            }
        ]

        answers = prompt(questions)
        headers = {
            'Accept': 'application/json',
        }

        response = requests.get(
            'https://api.dehashed.com/search?query=address:' + answers['address'],
            headers=headers,
            auth=(API_USERNAME, API_KEY),
        )
        print(response.json())
    
if __name__ == "__main__":
    app = Dehashed()
    choice = app.answers['choices']
    if choice == 'email':
        print(app.email())
    elif choice == 'phone':
        print(app.phone())
    elif choice == 'username':
        print(app.username())
    elif choice == 'address':
        print(app.address())