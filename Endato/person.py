import requests
from InquirerPy import prompt
from pprint import pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

PERSON_GALAXY_APP_NAME = os.environ['PERSON_GALAXY_APP_NAME']
PERSON_GALAXY_APP_PW = os.environ['PERSON_GALAXY_APP_PW']

class Person:
    
    def search(self):
        questions = [
        {
            "type": "input",
            "message": "First Name:",
            "name": "firstname",
        },
        {
            "type": "input",
            "message": "Middle Name:",
            "name": "middlename",
        },
        {
            "type": "input",
            "message": "Last Name:",
            "name": "lastname",
        },
        {
            "type": "input",
            "message": "City:",
            "name": "city",
        },
        {
            "type": "input",
            "message": "State::",
            "name": "state",
        },
        {
            "type": "input",
            "message": "Zip:",
            "name": "zip",
        },
        {
            "type": "input",
            "message": "Street:",
            "name": "street",
        },
        {
            "type": "input",
            "message": "DOB:",
            "name": "dob",
        },
        {
            "type": "input",
            "message": "Age:",
            "name": "age",
        },
        {
            "type": "input",
            "message": "Age Range (1-100):",
            "name": "agerange",
        },
        {
            "type": "input",
            "message": "Phone:",
            "name": "phone",
        },
        {
            "type": "input",
            "message": "Email:",
            "name": "email",
        },
        
        ]

        result = prompt(questions)
        
        url = "https://devapi.endato.com/PersonSearch"



        payload = {
            "FirstName": result['firstname'],
            "MiddleName": result['middlename'],
            "LastName": result['lastname'],
            "Addresses": [
                {
                    "City": result['city'],
                    "State": result['state'],
                    "Zip": result['zip'],
                    "AddressLine1": result['street'],
                    "AddressLine2": ""
                }
            ],
            "Dob": result['dob'],
            "Age": result['age'],
            "AgeRange": result['agerange'],
            "Phone": result['phone'],
            "Email": result['email'],
            "Includes": [
                "Addresses",
                "PhoneNumbers"
            ],
            "FilterOptions": [
                "IncludeLowQualityAddresses"
            ],
            "Page": 1,
            "ResultsPerPage": 10
        }
        headers = {
            "galaxy-ap-name": PERSON_GALAXY_APP_NAME,
            "galaxy-ap-password": PERSON_GALAXY_APP_PW,
            "content-type": "application/json",
            "galaxy-search-type": "Person"
        }

        response = requests.post(url, json=payload, headers=headers)

        return response.text
if __name__ == '__main__':
    app = Person.search()
    print(app.search())