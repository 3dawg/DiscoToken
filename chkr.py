import requests
import time
from colorama import Fore, init
import urllib
import http.server
import socketserver

PORT = 9067

#here we define the class to actually use the proxy
#Todo: Add SSL Functionality



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

#i added it here for now 
#here we define the class to actually use the proxy
#Todo: Add SSL Functionality

class MyProxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url=self.path[1: ]
        self.send_response(200)
        self.end_headers()
        self.copyfile(urllib.urlopen(url), self.wfile)
httpd = socketserver.TCPServer(('', PORT), MyProxy)
print ("Now serving at " + str(PORT))
httpd.serve_forever()
proxies = {
  'http': 'localhost:9067'
}
with open(f"{tknname}", "r") as f:
    for line in f:
        time.sleep(1)
        token = line.rstrip("\n")
        headers = {"Authorization": f"{token}"}
        src = requests.get("http://discordapp.com/api/v6/auth/login", headers=headers, proxies=proxies)

        try:
            if src.status_code == 200:
                print(f"{Fore.GREEN}[-] {Fore.RESET}Token Works! > " + token)
            else:
                print(f"{Fore.RED}[-] {Fore.RESET}Invalid Token. > " + token)
        except Exception:
            print("Something broke lmfao contact discord suppport or open an issue :)")
print("Finished checking!")

