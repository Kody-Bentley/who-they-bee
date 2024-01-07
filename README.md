# Who They Bee
 - Simple Python CLI application for OSINT

## Installation
Creating a virtual environment is recommended, afterwards install requirements from included requirements.txt file

```
pip install -r requirements.txt
```

## How to run

Most modules require you to have an account with an API key. You can simply sign up at the relevant site and there is a free trial for just about all of them. Eventually I will include a list with steps on how to obtain these resources, but for now you are on your own. All keys must be included in a .env file in the root of the project and include your keys in the following format. For now the naming convention for keys can be found in each respective module. Once you have added the appropriate keys you are good to go. Modules that do not require a key are the Google Dorks functionality, NMAP scanner, and Username Search, the rest require respective keys for the module to run.
```
REVERSE_PHONE_KEY = '<YOUR_API_KEY>'
REVERSE_EMAIL_KEY = '<YOUR_API_KEY>'
```

Once you have your .env file setup simply run
```
python main.py
```
from root directory and follow CLI prompts

## This is a work in progress

There are still a ton of things that need to be added, tweaked, and fixed. Proper error handling is still minimal at best, please keep that in mind.

## Known issues.
1) Username Search module sometimes hangs or will not complete.
2) Writing results to JSON file currently only works for the Person module.
3) Exiting the program does not behave correctly.
4) Many more im sure :D.
