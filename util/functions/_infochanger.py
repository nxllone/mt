#updating it in v2 (not working rn)
#dont mess with it

import requests
from ..functions._validator import token_checker
class username:
    def __init__(self):
        self.user = input("enter the new user : ")
        self.token = input("enter your token : ")

    def user_changer(self):
        if token_checker.checker(token=str(self.token)) == "valid":
            url = "https://discordapp.com/api/v6/users/@me"
            headers = {
            "Authorization": self.token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
            r = requests.post(url, headers=headers)
            print(r.json)
        else:
            print(f"token : {token_checker.checker(token=self.token)}")

user = username()