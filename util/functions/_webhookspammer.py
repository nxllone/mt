import requests
from time import sleep

count = 0
hook = input("enter your hook : ")
msg = input("enter your msg : ")
time = input("enter delay time -- lowest (0.1) : ")

class webhookspammer:
    def __init__(self):
        pass

    @staticmethod
    def spam():
        global count
        payload = {
            "content": f"{str(msg)}",
            "username": "DXR MULTI TOOL | http://dxrv.is-best.net/1.html"
        }
        r = requests.post(hook, json=payload)
        sleep(float(time))
        count+=1
        print("STARTED SPAMMING")
        print(f"\ndone {count} msgs\n")
        return webhookspammer.spam()