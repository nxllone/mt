import requests, os, random, string, threading, sys, json, asyncio
from colorama import init
from termcolor import cprint
from time import sleep
from util.plugins.ui import ui, menu, welcome
from util.plugins.version import version
from util.functions._tokenspammer import spammer
from util.functions._usersniper import Sniper
from util.functions._validator import token_checker
from util.functions._vanitysniper import vanity

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
cprint(menu(), "light_yellow")

choice = input("choose ~~> ")

if choice == "changeuser":
    newuser = input("New username: ")

    with open("dxrconfig.json", "r", newline='\n') as _configfile:
        data = json.load(_configfile)

    data["username"] = str(newuser)

    with open("dxrconfig.json", "w", newline='\n') as _configfile:
        json.dump(data, _configfile)

    cprint(f"Username changed to: {newuser}", "light_green")
    sleep(2)

if choice == "webhook":
    webhook = input("enter your webhook: ")

    with open("dxrconfig.json", "r", newline='\n') as _configfile:
        data = json.load(_configfile)

    data["webhook"] = str(webhook)

    with open("dxrconfig.json", "w", newline='\n') as _configfile:
        json.dump(data, _configfile)

    cprint(f"webhook changed to: {webhook}", "light_green")
    sleep(2)

if int(choice) == 1:
    vanit_stealer_choice = input("1 - vanity stealer\n2 - go back : \n\n ~~> ")
    if int(vanit_stealer_choice) == 1:
        vanityy = vanity()
if int(choice) == 2:
    nitro_stealer_choice = cprint("soon...", "light_red")
    sleep(2)
if int(choice) == 3:
    user_stealer_choice = input("1 - user sniper\n2 - go back : \n\nchoice ~~> ")
    if int(user_stealer_choice) == 1:
        snipper = Sniper()
if int(choice) == 4:
    tokens_stealer_choice = input("1 - tokens spamming tool\n2 - create tokens file\n3 - add a token\n\nchoice ~~> ")
    if int(tokens_stealer_choice) == 1:
        chan = input("channel id : ")
        msg = input("your msg : ")
        for i in range(10):
            thread = threading.Thread(target=spammer.token_uploader, args=(msg, chan))
            thread.start()
    elif int(tokens_stealer_choice) == 2:
        if os.path.exists(os.path.join(os.getenv("TEMP")+"\\tokens.txt")):
            cprint("tokens file alr excist retard", "light_red")
            print("path : ", os.path.join(os.getenv("TEMP")+"\\tokens.txt"))
            sleep(2)
        else:
            with open(os.path.join(os.getenv("TEMP")+"\\tokens.txt"), "w", newline='\n') as f:
                f.write("#dexr on top\n")
                f.close()
                cprint("file created in temp dir", "light_green")
                print("path : ", os.path.join(os.getenv("TEMP")+"\\tokens.txt"))
                sleep(2)
    elif int(tokens_stealer_choice) == 3:
        if os.path.exists(os.path.join(os.getenv("TEMP")+"\\tokens.txt")):
            token = input("enter your token : ")
            with open(os.path.join(os.getenv("TEMP")+"\\tokens.txt"), "a", newline='\n') as f:
                f.writelines(f"{token}\n")
            cprint(f"done | {token}: has been added", "light_green")
            sleep(2)
if int(choice) == 5:
    token_checker()
    print("\n\n waiting 5 secs...")
    sleep(5)
