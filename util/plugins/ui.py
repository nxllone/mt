from colorama import Fore

def ui(version, user, webhook):
    return f"""     
                                         ══════════════════════════════
your webhook - {webhook}
                                         ══════════════════════════════

                                            ▓█████▄ ▒██   ██▒ ██▀███  
                                            ▒██▀ ██▌▒▒ █ █ ▒░▓██ ▒ ██▒
                                            ░██   █▌░░  █   ░▓██ ░▄█ ▒
                                            ░▓█▄   ▌ ░ █ █ ▒ ▒██▀▀█▄            @8.3m
                                            ░▒████▓ ▒██▒ ▒██▒░██▓ ▒██▒          version - {version}
                                            ▒▒▓  ▒ ▒▒ ░ ░▓ ░░ ▒▓ ░▒▓░           user - {user}
                                            ░ ▒  ▒ ░░   ░▒ ░  ░▒ ░ ▒░           
                                            ░ ░  ░  ░    ░    ░░   ░ 
                                            ░     ░    ░     ░     
                                            ░                                                    
                            """               


def welcome():
    return f"""                                                                                                                                                            
┌─┐┌┐┌┌┬┐┌─┐┬─┐  ┬ ┬┌─┐┬ ┬┬─┐  ┬ ┬┌─┐┌─┐┬─┐
├┤ │││ │ ├┤ ├┬┘  └┬┘│ ││ │├┬┘  │ │└─┐├┤ ├┬┘
└─┘┘└┘ ┴ └─┘┴└─   ┴ └─┘└─┘┴└─  └─┘└─┘└─┘┴└─       
\n
\n                          
                            """               


def menu():
    return f""" 
                                            ╔══════════════════════╔
                                            ║   (1) vanity cmds    ║ 
                                            ║   (2) Nitro cmds     ║
                                            ║   (3) sniper cmds    ║    
                                            ║   (4) spammer cmds   ║ 
                                            ║   (5) tokens cmds    ║
                                            ╚══════════════════════╩
                                    ╔═══════════════════════════════════════╦
                                    ║           additonal cmds :            ║
                                    ║    ~changeuser  (change your user)    ║
                                    ║    ~webhook  (make a static webhook)  ║
                                    ║    ~theme  (not working)              ║
                                    ╚═══════════════════════════════════════╩
                                            ░ ▒  ▒ ░░   ░▒ ░  ░▒ ░ ▒░
                                            ░ ░  ░  ░    ░    ░░   ░ 
                                            ░     ░    ░     ░     
                                            ░                                                                          
                """