from googlesearch import search
# from PyInquirer import style_from_dict, Token, prompt

def dorks_search(query, num_pages):
    for result in search(query, num_results=int(num_pages)):
        print(f'Result: {result}')