import requests as req
from PyInquirer import style_from_dict, prompt, Token
from pprint import pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

API_KEY_EMAIL = os.environ.get("REVERSE_EMAIL_KEY")

class ReverseEmail:
    def __init__(self, STYLE):
        self.STYLE = STYLE

    def get_email(self):
        questions = [
            {
                'type': 'input',
                'name': 'email',
                'message': 'Enter email to lookup...',
            }
        ]

        answers = prompt(questions, style=self.STYLE)
        r = req.get(f'https://api.ekata.com/4.1/email?api_key={API_KEY_EMAIL}&email_address={answers["email"]}')
        return r.json()

if __name__ == '__main__':
    question = {
        'type': 'input',
        'name': 'email_api',
        'message': 'Please supply Ekata API Key',
    }
    answer = prompt(question)
    app = ReverseEmail(API_KEY_EMAIL=answer['email_api'], STYLE=None)
    print(app.get_email())
