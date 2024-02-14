import requests, os, random, string, threading, sys
from colorama import init
from termcolor import cprint
from time import sleep

init()

token_list = []

class spammer:
    def __init__(self):
        pass

    def token_uploader(msg, id):
        with open(os.path.join(os.getenv("TEMP")+"\\tokens.txt"), 'r')as f:
            tokens = f.readlines()
            for line in tokens:
                token_list.append(line.replace("\n", ""))
        token = random.choice(token_list)
        url = f"https://discord.com/api/v9/channels/{id}/messages"
        headers = {
            "authorization": f"{token}"
        }
        payload = {
            "content": f"".join(random.choice("1234567890")for _ in range(3))+ f" {msg}"
        }
        r = requests.post(url, headers=headers, json=payload, )
        if r.status_code != 200:
            cprint(token, "light_red")
            spammer.token_uploader(id, msg)
        else:
            cprint(token, "light_green")
            spammer.token_uploader(id, msg)
