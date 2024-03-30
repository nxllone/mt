import requests, os, random, string, threading, sys, json, asyncio
from colorama import *
from termcolor import cprint
from time import sleep
from util.plugins.ui import ui, welcome
from util.plugins.version import version
from util.functions._tokenspammer import spammer
from util.functions._usersniper import Sniper
from util.functions._validator import token_checker
from util.functions._vanitysniper import vanity
from util.functions._tokenschecker import server_check
from util.functions._tokenkick import token_kick
import pystyle

init()

if not os.path.exists("dxrconfig.json"):
    _configfile = open("dxrconfig.json", "w", newline='\n')
    cprint(welcome(), "light_red")
    user = input("User (username) > ")
    hook = input("hook (webhook) > ")
    user_data = {
        "username": f"{user}",
        "webhook": f"{hook}"
    }
    with open("dxrconfig.json", "w", newline='\n') as _configfile:
        json.dump(user_data, _configfile, indent=2)
        print(f"Data written to file: {_configfile.name}")

with open("dxrconfig.json", "r", newline='\n') as _configfile:
    data = json.load(_configfile)
    username = data["username"]
    cordhook = data["webhook"]

cprint(ui(version(), username, cordhook), "red")

choice = 0
choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Choice: ")

if int(choice) == 1:
    token_checker()
    sleep(3)

if int(choice) == 2:
    from util.functions._webhookspammer import *
    for i in range (2):
        thwebspam = threading.Thread(target=webhookspammer.spam, args=())
        thwebspam.start()

if int(choice) == 3:
    from util.functions._webhookdeleter import *
    print(delete.delete())

if int(choice) == 4:
    from util.functions._webhookmemer import *
    for i in range (1):
        thread1 = threading.Thread(target=memer.load_meme, args=())
        thread2 = threading.Thread(target=memer.load_meme, args=())
        thread3 = threading.Thread(target=memer.load_meme, args=())
        thread1.start()
        thread2.start()
        thread3.start()

if int(choice) == 5:
    server_check()
    print("exting after 5 secs...")
    sleep(5)

if int(choice) == 6:
    token_kick()
    print("exting after 5 secs...")
    sleep(5)

if int(choice) == 7:
    chan = input("channel id : ")
    msg = input("your msg : ")
    for i in range(10):
        thread = threading.Thread(target=spammer.token_uploader, args=(msg, chan))
        thread.start()

if int(choice) == 8:
    snipper = Sniper()

if int(choice) == 9:
    vanityy = vanity()

if int(choice) == 10:
    print("soon :)")
    sleep(5)

if int(choice) == 11:
    if os.path.exists(os.path.join(os.getenv("TEMP")+"\\tokens.txt")):
        cprint("tokens file alr excist retard", "light_red")
        print("path : ", os.path.join(os.getenv("TEMP")+"\\tokens.txt"))
        sleep(3)
    else:
        with open(os.path.join(os.getenv("TEMP")+"\\tokens.txt"), "w", newline='\n') as f:
            f.close()
            cprint("file created in temp dir", "light_green")
            print("path : ", os.path.join(os.getenv("TEMP")+"\\tokens.txt"))
            sleep(3)

if int(choice) == 12:
    if os.path.exists(os.path.join(os.getenv("TEMP")+"\\tokens.txt")):
        token = input("enter your token : ")
        with open(os.path.join(os.getenv("TEMP")+"\\tokens.txt"), "a", newline='\n') as f:
            f.writelines(f"{token}\n")
        cprint(f"done | {token}: has been added", "light_green")
        sleep(3)

if int(choice) == 13:
    if os.path.exists(os.path.join(os.getenv("TEMP")+"\\tokens.txt")):
        os.remove(os.path.join(os.getenv("TEMP")+"\\tokens.txt")) 
        cprint(f"File has been cleared", "light_green")
        with open(os.path.join(os.getenv("TEMP")+"\\tokens.txt"), "w", newline='\n') as f:
            f.close()
        sleep(3)
    else:
        print(f"{Fore.RED} Couldn't find the tokens file.. create a new one")
        sleep(3)

if int(choice) == 14:
    print(f"{Fore.RED} That option is for vip tool only")
    sleep(5)