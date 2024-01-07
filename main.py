import requests as requests
from pprint import pprint
import os
import re
import sys
from InquirerPy import prompt
from Reverse_Phone import reverse_phone
from Endato import reverse_email
from Endato import person
from Dehashed import dehashed
from Scrapers import dorks
from Scanners import nmap_scanner as scanner
from Socials.Username_search import search
from pyfiglet import Figlet
import asyncio
import json

def main():
    custom_fig = Figlet(font='graffiti')
    print(custom_fig.renderText('Who They Bee'))

    questions = [

        {
            'type': 'list',
            'name': 'modules',
            'message': 'What module would you like to run?',
            'choices': ['Reverse Phone', 'Reverse Email', 'Dorks', 'Port Scanner', 'Dehashed', 'Person', 'Username Checker'],
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
            questions = [
                {
                    'type': 'list',
                    'name': 'output',
                    'message': 'Would you like to run another search?',
                    'choices': ['Yes', 'No'],
                    'filter': lambda val: val.lower()
                }
            ]
            if prompt(questions)['output'] == 'yes':
                main()
            else:
                sys.exit(1)
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
                file.write(json.dumps(reverse_email.ReverseEmail().get_email(), indent=4, sort_keys=True))
                print(f'Data written to file "output.txt"...')
                file.close()
        else:
            pprint(reverse_email.ReverseEmail().get_email())
            questions = [
                {
                    'type': 'list',
                    'name': 'output',
                    'message': 'Would you like to run another search?',
                    'choices': ['Yes', 'No'],
                    'filter': lambda val: val.lower()
                }
            ]
            if prompt(questions)['output'] == 'yes':
                main()
            else:
                sys.exit(1)
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
        
        questions = [
                {
                    'type': 'list',
                    'name': 'output',
                    'message': 'Would you like to run another search?',
                    'choices': ['Yes', 'No'],
                    'filter': lambda val: val.lower()
                }
            ]
        if prompt(questions)['output'] == 'yes':
            main()
        else:
            sys.exit(1)
    elif answers['modules'] == 'port scanner':
        full_results = [re.findall('^[\w\?\.]+|(?<=\s)\([\d\.]+\)|(?<=at\s)[\w\:]+', i) for i in os.popen('arp -a')]
        final_results = [dict(zip(['IP', 'LAN_IP', 'MAC_ADDRESS'], i)) for i in full_results]
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
        
        questions = [
                {
                    'type': 'list',
                    'name': 'output',
                    'message': 'Would you like to run another search?',
                    'choices': ['Yes', 'No'],
                    'filter': lambda val: val.lower()
                }
            ]
        if prompt(questions)['output'] == 'yes':
            main()
        else:
            sys.exit(1)
    elif answers['modules'] == 'dehashed':
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
            module = dehashed.Dehashed.modules()
            if module == 'email':
                dehashed.Dehashed.email(self=dehashed)
                questions = [
                {
                    'type': 'list',
                    'name': 'output',
                    'message': 'Would you like to run another search?',
                    'choices': ['Yes', 'No'],
                    'filter': lambda val: val.lower()
                }
            ]
                if prompt(questions)['output'] == 'yes':
                    main()
                else:
                    sys.exit(1)
            elif module == 'phone':
                dehashed.Dehashed.phone(self=dehashed)
                questions = [
                {
                    'type': 'list',
                    'name': 'output',
                    'message': 'Would you like to run another search?',
                    'choices': ['Yes', 'No'],
                    'filter': lambda val: val.lower()
                }
            ]
                if prompt(questions)['output'] == 'yes':
                    main()
                else:
                    sys.exit(1)
            elif module == 'address':
                dehashed.Dehashed.address(self=dehashed)
                questions = [
                {
                    'type': 'list',
                    'name': 'output',
                    'message': 'Would you like to run another search?',
                    'choices': ['Yes', 'No'],
                    'filter': lambda val: val.lower()
                }
            ]
                if prompt(questions)['output'] == 'yes':
                    main()
                else:
                    sys.exit(1)
            elif module == 'username':
                dehashed.Dehashed.username(self=dehashed)
                questions = [
                {
                    'type': 'list',
                    'name': 'output',
                    'message': 'Would you like to run another search?',
                    'choices': ['Yes', 'No'],
                    'filter': lambda val: val.lower()
                }
            ]
                if prompt(questions)['output'] == 'yes':
                    main()
                else:
                    sys.exit(1)
    elif answers['modules'] == 'person':
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
            with open('./Output/person.json', 'w') as file:
                raw = json.loads(person.Person.search(self=person))
                file.write(json.dumps(raw, indent=4, sort_keys=True))
                print(f'Data written to file "person.json"...')
                file.close()
        else:
            print(person.Person.search(self=person))
            
            questions = [
                {
                    'type': 'list',
                    'name': 'output',
                    'message': 'Would you like to run another search?',
                    'choices': ['Yes', 'No'],
                    'filter': lambda val: val.lower()
                }
            ]
            if prompt(questions)['output'] == 'yes':
                main()
            else:
                sys.exit(1)
    elif answers['modules'] == 'username checker':
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
            with open('./Output/username_search.json', 'w') as file:
                raw = json.loads(person.Person.search(self=person))
                file.write(json.dumps(raw, indent=4, sort_keys=True))
                print(f'Data written to file "person.json"...')
                file.close()
        else:
            questions = [
            {
                'type': 'input',
                'name': 'username',
                'message': 'Input Username To Search',
                'filter': lambda val: val.lower()
            }
        ]
            answers = prompt(questions)
            
            loop = asyncio.get_event_loop()
            print(loop.run_until_complete(search.UserSearch.main(answers['username'])))
        
            questions = [
                {
                    'type': 'list',
                    'name': 'output',
                    'message': 'Would you like to run another search?',
                    'choices': ['Yes', 'No'],
                    'filter': lambda val: val.lower()
                }
            ]
            if prompt(questions)['output'] == 'yes':
                main()
            else:
                sys.exit(1)        

if __name__ == '__main__':
    main()
