import requests as req
from InquirerPy import prompt
import os
from os.path import join, dirname
from dotenv import load_dotenv
from twilio.rest import Client

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

ACCOUNT_SID = os.environ['TWILIO_SID']
ACCOUNT_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
client = Client(ACCOUNT_SID, ACCOUNT_AUTH_TOKEN)

# questions = []

class ReversePhone:
    def get_num(self):
        questions = [
            {
                'type': 'input',
                'name': 'phone',
                'message': 'Enter phone number to lookup...',
            }
        ]

        answers = prompt(questions)
        
        phone_number = client.lookups.v1.phone_numbers(answers['phone']).fetch(add_ons="trestle_reverse_phone")

        
        attributes = {
            "number": phone_number.phone_number,
            "carrier":phone_number.carrier,
            "country": phone_number.country_code,
            "caller_name": phone_number.caller_name,
            "url": phone_number.url,
            "add_ons": phone_number.add_ons,

        }

        return attributes

# if __name__ == "__main__":
#     app = ReversePhone()
#     # print(app.get_num())
