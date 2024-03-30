import requests, colorama

class server_check:
    def __init__(self):
        self.token = input("enter your token: ")
        self.id = input("enter any channel id from server: ")
        server_check.checker(self, self.token, self.id)

    def checker(self, token, id):
        headers = {
            "authorization": f"{token}"
        }
        r = requests.get(f"https://discord.com/api/v9/channels/{id}/messages?limit=50", headers=headers)
        if r.ok:
            print(f"{colorama.Fore.GREEN}Token is in the server")
        else:
            print(f"{colorama.Fore.RED}Token is not the server")
