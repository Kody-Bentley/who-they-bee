import requests as req
from PyInquirer import style_from_dict, prompt, Token
from pprint import pprint

class ReverseEmail:
    def __init__(self, API_KEY_EMAIL, STYLE):
        self.API_KEY_EMAIL = API_KEY_EMAIL
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
        r = req.get(f'https://api.ekata.com/3.3/identity_check?api_key=XXXXX&primary.name=Waidong+L+Syrws&primary.phone=2069735100&primary.email_address=waidong%40gmail.com&primary.address.street_line_1=100+Syrws+St&primary.address.street_line_2=Ste+1&primary.address.city=Lynden&primary.address.state_code=WA&primary.address.postal_code=98264&primary.address.country_code=US&ip_address=54.190.251.42&secondary.firstname=Waanataa&secondary.lastname=Labarrete&secondary.phone=2061115101&secondary.email_address=syrwspizza%40example.com&secondary.address.line_1=1+Syrws+St%2C+Lynden%2C+WA&secondary.address.country_code=US')
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
