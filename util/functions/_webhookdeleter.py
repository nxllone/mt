import requests
from time import sleep

hook = input("enter your hook : ")

class delete:
    def __init__(self):
        pass

    @staticmethod
    def delete():
        r = requests.delete(f"{hook}")
        if r.ok:
            print("WEBHOOK DELETED")
            sleep(3)
        else:
            print("WEBHOOK DOESNT EXCIST")
            sleep(3) 