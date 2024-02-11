import requests, os, random, string, threading, sys
from colorama import *
from time import sleep
from src import spammer, Sniper, vanity
from src.utils.ui import ui, menu
from src.utils.version import version
print(ui(version()))
print(menu())

choice = input("choose ~~> ")

if int(choice) == 1:
    print("\033c", end='')
    vanit_stealer_choice = input("1 - vanity stealer\n2 - go back : \n\n ~~> ")
    if int(vanit_stealer_choice) == 1:
        print("\033c", end='')
        vanityy = vanity()
    else:
        print("\033c", end='')
        os.execv(sys.executable, ['python'] + sys.argv)
if int(choice) == 2:
    print("\033c", end='')
    nitro_stealer_choice = print("soon...")
    sleep(2)
    print("\033c", end='')
    os.execv(sys.executable, ['python'] + sys.argv)
if int(choice) == 3:
    print("\033c", end='')
    user_stealer_choice = input("1 - user sniper\n2 - go back : \n\nchoice ~~> ")
    if int(user_stealer_choice) == 1:
        print("\033c", end='')
        snipper = Sniper()
    else:
        print("\033c", end='')
        os.execv(sys.executable, ['python'] + sys.argv)
if int(choice) == 4:
    print("\033c", end='')
    tokens_stealer_choice = input("1 - tokens spamming tool\n2 - create tokens file\n\nchoice ~~> ")
    if int(tokens_stealer_choice) == 1:
        print("\033c", end='')
        id = input("channel id : ")
        msg = input("msg : ")
        for i in range(10):
            thread = threading.Thread(target=spammer.token_uploader, args=(id, msg))
            thread.start()
    elif int(tokens_stealer_choice) == 2:
        if os.path.exists("tokens.txt"):
            print("tokens file alr excist retard")
            sleep(2)
            print("\033c", end='')
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            with open("tokens.txt", "a")as f:
                f.writelines("#dexr on top\n")
                f.close()
                print("file created in same dir")
                sleep(2)
                print("\033c", end='')
                os.execv(sys.executable, ['python'] + sys.argv)