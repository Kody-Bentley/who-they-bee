# Who They Bee
 - Simple Python CLI application for OSINT

## Installation
Creating a virtual environment is recommended, afterwards install requirements from included requirements.txt file

```
pip install -r requirements.txt
```

## How to run

Modules for reverse phone/email lookup require an API key from https://ekata.com/ once obtained include a .env file in the project root directory with your API keys as such 
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
