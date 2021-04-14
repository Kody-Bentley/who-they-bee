import requests as requests


from pprint import pprint
import os
import re
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
from Reverse_Phone import reverse_phone
from Reverse_Email import reverse_email
from Scrapers import dorks
from Scanners import nmap_scanner as scanner
import json



STYLE = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: "#243657",
})

def main():

    questions = [

        {
            'type': 'list',
            'name': 'modules',
            'message': 'What module would you like to run?',
            'choices': ['Reverse Phone', 'Reverse Email', 'Dorks', 'Port Scanner'],
            'filter': lambda val: val.lower()
        },
    ]

    answers = prompt(questions)
    if answers['modules'] == 'reverse phone':
        questions = [
            {
                'type': 'list',
                'name': 'output',
                'message': 'Would you like to output data to JSON file?',
                'choices': ['Yes', 'No'],
                'filter': lambda val: val.lower()
            }
        ]
        if prompt(questions)['output'] == 'yes':
            with open('output.txt', 'w') as file:
                file.write(json.dumps(reverse_phone.ReversePhone.get_num(self=reverse_phone), indent=4, sort_keys=True))
                print(f'Data written to file "output.txt"...')
                file.close()
        else:
            pprint(reverse_phone.ReversePhone.get_num(self=reverse_phone))
    elif answers['modules'] == 'reverse email':
        questions = [
            {
                'type': 'list',
                'name': 'output',
                'message': 'Would you like to output data to JSON file?',
                'choices': ['Yes', 'No'],
                'filter': lambda val: val.lower()
            }
        ]
        if prompt(questions)['output'] == 'yes':
            with open('output.txt', 'w') as file:
                file.write(json.dumps(reverse_email.ReverseEmail(STYLE=STYLE).get_email(), indent=4, sort_keys=True))
                print(f'Data written to file "output.txt"...')
                file.close()
        else:
            pprint(reverse_email.ReverseEmail(STYLE=STYLE).get_email())
    elif answers['modules'] == 'dorks':
        questions = [{
            'type': 'input',
            'name': 'query',
            'message': 'Query to search...',
        },
            {
                'type': 'input',
                'name': 'num_pages',
                'message': 'Number of pages to return...'
            }]
        answers = prompt(questions)
        dorks.dorks_search(answers['query'], answers['num_pages'])
    elif answers['modules'] == 'port scanner':
        full_results = [re.findall('^[\w\?\.]+|(?<=\s)\([\d\.]+\)|(?<=at\s)[\w\:]+', i) for i in os.popen('arp -a')]
        final_results = [dict(zip(['IP', 'LAN_IP', 'MAC_ADDRESS'], i)) for i in full_results]
        final_results = [{**i, **{'LAN_IP': i['LAN_IP'][1:-1]}} for i in final_results]
        print(f'Final results: {final_results}')
        questions = [{
            'type': 'input',
            'name': 'ip',
            'message': 'Target IP...'
        },
            {
                'type': 'input',
                'name': 'ports',
                'message': 'Port range to scan...'
            }

        ]
        answers = prompt(questions)
        scanner.default_scanner(answers['ip'], answers['ports'])


if __name__ == '__main__':
    main()
