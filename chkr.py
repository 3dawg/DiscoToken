import requests
import time
from colorama import Fore, init

print(
    f"""{Fore.GREEN}
 /$$$$$$$ /$$                        /$$$$$$$$      /$$
| $$__  $|__/                       |__  $$__/     | $$
| $$  \ $$/$$ /$$$$$$$ /$$$$$$$ /$$$$$$| $$ /$$$$$$| $$   /$$ /$$$$$$ /$$$$$$$
| $$  | $| $$/$$_____//$$_____//$$__  $| $$/$$__  $| $$  /$$//$$__  $| $$__  $$
| $$  | $| $|  $$$$$$| $$     | $$  \ $| $| $$  \ $| $$$$$$/| $$$$$$$| $$  \ $$
| $$  | $| $$\____  $| $$     | $$  | $| $| $$  | $| $$_  $$| $$_____| $$  | $$
| $$$$$$$| $$/$$$$$$$|  $$$$$$|  $$$$$$| $|  $$$$$$| $$ \  $|  $$$$$$| $$  | $$
|_______/|__|_______/ \_______/\______/|__/\______/|__/  \__/\_______|__/  |__/


                                                                              
{Fore.RED}V 0.0.1{Fore.GREEN}
[-] Made with {Fore.RED}<3{Fore.GREEN} by Daddie

Note: You should {Fore.RED}NEVER{Fore.GREEN} do more than 50 tokens at once because discord will rate limit you
Ps: This tool is made for educational purposes only I am not liable for any actions you do while using this
"""
)
tknname = input("Drag and drop your tokenlist: ")
with open(f"{tknname}", "r") as f:
    for line in f:
        time.sleep(1)
        token = line.rstrip("\n")
        headers = {"Authorization": f"{token}"}
        src = requests.get("https://discordapp.com/api/v6/auth/login", headers=headers)

        try:
            if src.status_code == 200:
                print(f"{Fore.GREEN}[-] {Fore.RESET}Token Works! > " + token)
            else:
                print(f"{Fore.RED}[-] {Fore.RESET}Invalid Token. > " + token)
        except Exception:
            print("Something broke lmfao contact discord suppport or open an issue :)")
print("Finished checking!")
