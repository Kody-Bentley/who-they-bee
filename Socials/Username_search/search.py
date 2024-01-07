from Socials.Username_search.social_networks import links
import asyncio
from time import time
import aiohttp

class UserSearch:
    async def get(url, session, username, social_network):
        global results
        results = {}
        url = url.format(username)
        try:
            async with session.get(url) as response:
                print('\033[33m[!] {:10}: {}\033[0m\033[J'.format(social_network, url), end='\r')
                if response.status == 200:
                    print('\033[32m[+] {:10}: {}\033[0m\033[J'.format(social_network, url))
                    results[social_network] = url
                else:
                    pass
            return response.release()
        except:
            pass


    async def main(username):
        # start = time()
        async with aiohttp.ClientSession() as session:
            tasks = [
                await UserSearch.get(url, session, username, social_network)
                for social_network, url in links.items() 
            ]
            res = await asyncio.gather(*tasks)
        return res