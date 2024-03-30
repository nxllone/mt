import requests, os
from colorama import init
from termcolor import cprint

init()

class token_checker:
    def __init__(self):
        self.pick = input("1 - check one token\n2 - filter tokens in file\n\nchoice ~~>")
        self.choice()

    @staticmethod
    def checker(token):
        url = "https://discord.com/api/v9/users/@me/settings"
        headers = {
            "Authorization": str(token),
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return cprint(f"{token} | valid", "light_green")
        elif "You need to verify your account in order to perform this action." in r.text:
            return cprint(f"{token} | locked", "light_red")
        elif "Unauthorized" in r.text:
            return cprint(f"{token} | invalid", "light_red")
        else:
            return cprint(f"{token} | error", "light_yellow")

    def choice(self):
        if str(self.pick) == "1":
            token = input("enter your token : ")
            token_checker.checker(token)
        elif str(self.pick) == "2":
            with open(os.path.join(os.getenv("TEMP")+"\\tokens.txt"), "r") as f:
                tokens = f.readlines()
                for tokenn in tokens:
                    print(token_checker.checker(tokenn.strip())) 