from colorama import *
from pystyle import *

def ui(version, user, webhook):
    banner =    f"""{Fore.LIGHTMAGENTA_EX}
                            ██████╗ ██╗  ██╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     
                            ██╔══██╗╚██╗██╔╝██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
                            ██║  ██║ ╚███╔╝ ██████╔╝       ██║   ██║   ██║██║   ██║██║     
                            ██║  ██║ ██╔██╗ ██╔══██╗       ██║   ██║   ██║██║   ██║██║     
                            ██████╔╝██╔╝ ██╗██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
                            ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝                                                           

                                 version {Fore.RED}{version}            |         {Fore.RESET}user {Fore.CYAN}{user}{Fore.RESET}                                                            
                                                                                {Fore.RESET}"""
    print(f"Webhook :""     ", f"{Fore.LIGHTMAGENTA_EX}{webhook}{Fore.RESET}","\n\n")
    print(banner)
    print("                               ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}1{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Checker{Fore.LIGHTMAGENTA_EX}]", "     ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}8{Fore.LIGHTMAGENTA_EX}>>  [{Fore.RESET}User Sniper{Fore.LIGHTMAGENTA_EX}]" )
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}2{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Webhook Spammer{Fore.LIGHTMAGENTA_EX}]", "   ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}9{Fore.LIGHTMAGENTA_EX}>>  [{Fore.RESET}Vanity Sniper{Fore.LIGHTMAGENTA_EX}]" )
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}3{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Webhook Deleter{Fore.LIGHTMAGENTA_EX}]", "   ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}10{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Nitro Gen{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}4{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Webhook Memer{Fore.LIGHTMAGENTA_EX}]", "    ", f" {Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}11{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Create Tokens File{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}5{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Guild Checker{Fore.LIGHTMAGENTA_EX}]", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}12{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Add Token To File{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}6{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Guild Leaver{Fore.LIGHTMAGENTA_EX}]",  "", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}13{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Clear Token File{Fore.LIGHTMAGENTA_EX}]")
    print("                               ",f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}7{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Token Spammer{Fore.LIGHTMAGENTA_EX}]", "     ", f"{Fore.LIGHTMAGENTA_EX}<<{Fore.RESET}14{Fore.LIGHTMAGENTA_EX}>> [{Fore.RESET}Next Page{Fore.LIGHTMAGENTA_EX}]")



def welcome():
    return f"""                                                                                                                                                            
┌─┐┌┐┌┌┬┐┌─┐┬─┐  ┬ ┬┌─┐┬ ┬┬─┐  ┬ ┬┌─┐┌─┐┬─┐
├┤ │││ │ ├┤ ├┬┘  └┬┘│ ││ │├┬┘  │ │└─┐├┤ ├┬┘
└─┘┘└┘ ┴ └─┘┴└─   ┴ └─┘└─┘┴└─  └─┘└─┘└─┘┴└─       
\n
\n                          
                            """               