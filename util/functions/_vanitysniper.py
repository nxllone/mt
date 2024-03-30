import requests
from time import sleep

class vanity:
    def __init__(self):
        self.hook = input("enter your webhook : ")
        self.token = input("enter your token : ")
        self.vanityyy = input("vanity : ")
        self.server = input("server id : ")
        self.header = {
            "authorization": self.token,
        }
        self.payload = { "code": self.vanityyy }
        self.vanity_stealer()

    def vanity_stealer(self):
        return self.change_vanity()

    def change_vanity(self):
        r = requests.patch(f"https://discord.com/api/v10/guilds/{self.server}/vanity-url", headers=self.header, json=self.payload)
        print(r.status_code)
        if r.status_code != 200:
             print("faild trying again...")
             sleep(5)
             self.change_vanity()
        else:
             requests.post(self.hook, json={"content": f"{self.vanityyy} got snipped @here"})
             exit()