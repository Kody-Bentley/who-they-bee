import requests
from InquirerPy import prompt
from pprint import pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

GALAXY_APP_NAME = os.environ.get("EMAIL_GALAXY_APP_NAME")

GALAXY_APP_PW = os.environ.get("EMAIL_GALAXY_APP_PW")

print(GALAXY_APP_PW, GALAXY_APP_NAME)

class ReverseEmail:
    
    def get_email(self):
        questions = [
            {
                'type': 'input',
                'name': 'email',
                'message': 'Enter email to lookup...',
            }
        ]

        answers = prompt(questions)

        url = "https://devapi.endato.com/Email/Enrich"

        payload = { "Email": answers["email"] }

        headers = {
            "accept": "application/json",
            "galaxy-ap-name": GALAXY_APP_NAME,
            "galaxy-ap-password": GALAXY_APP_PW,
            "content-type": "application/json",
            "galaxy-search-type": "DevAPIEmailID"
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response.text)

if __name__ == '__main__':
    app = ReverseEmail.get_email()
    print(app.get_email())
