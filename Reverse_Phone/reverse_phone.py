import requests as req
from PyInquirer import style_from_dict, prompt, Token
from pprint import pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

STYLE = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: "",
})
questions = []
API_KEY_PHONE = os.environ.get("REVERSE_PHONE_KEY")


class ReversePhone:
    def get_num(self):
        questions = [
            {
                'type': 'input',
                'name': 'phone',
                'message': 'Enter phone number to lookup...',
            }
        ]

        answers = prompt(questions, style=STYLE)
        r = req.get(f'https://api.ekata.com/3.1/phone?api_key={API_KEY_PHONE}&phone={answers["phone"]}')
        return r.json()

if __name__ == "__main__":
    app = ReversePhone()
    print(app.get_num())
