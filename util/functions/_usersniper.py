import random, requests, string, json
from time import sleep
from colorama import init
from termcolor import cprint

init()

class Sniper:
    def __init__(self):
        self.hook = self.webhook()
        self.token = input("enter your token : ")
        self.count = input("How many characters do you want the username to have: ")
        self.gen_user()
        self.check_user()
    
    def webhook(self):
        with open("dxrconfig.json", "r", newline='\n')as f:
            data = json.load(f)
            hook = data["webhook"]
            return hook

    def gen_user(self):
        self.user = "".join(random.choice(string.ascii_letters + string.digits + "._") for _ in range(int(self.count))).lower()

    def check_user(self):
        headers = {
            "Authorization": self.token,
        }
        payload = {"username": f"{self.user}"}

        r = requests.post("https://discord.com/api/v9/users/@me/pomelo-attempt", headers=headers, json=payload)
        raw = r.json()
        response = raw["taken"]

        if response:
            cprint(self.user, "light_green")
            requests.post(self.hook, json={"content": f"User taken ```{self.user}```"})
            sleep(1)
            self.gen_user()
            self.check_user()
        else:
            cprint(self.user, "light_green")
            requests.post(self.hook, json={"content": f"User is free ```{self.user}```@here"})
            sleep(1)
            self.gen_user()
            self.check_user()