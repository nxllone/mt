import requests, colorama

class token_kick:
    def __init__(self):
        self.token = input("enter your token: ")
        self.id = input("enter server id: ")
        token_kick.kicker(self, self.token, self.id)

    def kicker(self, token, id):
        headers = {
            "authorization": f"{token}"
        }
        r = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{id}", headers=headers)
        if r.ok:
            print(f"{colorama.Fore.GREEN}Token left the server")
        else:
            print(f"{colorama.Fore.RED}Token is not in the server")