import requests as r
from colorama import Fore
import os

os.system("clear")

print(Fore.GREEN + "╦╔═╗  ╔╦╗╦═╗╔═╗╔═╗╦╔═            ")
print("║╠═╝   ║ ╠╦╝╠═╣║  ╠╩╗        ")
print("╩╩     ╩ ╩╚═╩ ╩╚═╝╩ ╩        ")

print("""
|------------------------------|
| Dev: <UglyDev/>              |
| Page: Ugly Dev               |
|------------------------------|
""")
ip = input("[$] Enter target IP: ")

api = input("[$] Enter your API: ")

url = "https://api.ipfind.com/?ip={}&auth={}".format(ip,api)

req = r.get(url)
print("result: ")
print("   ")
print(req.json())
