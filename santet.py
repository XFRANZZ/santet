#!/usr/bin/env python3
# Auhor by Franz
# last update: 19/07/2021

import os, time, sys, json, socket, requests
from googlesearch import search
from getpass import getpass
from random import choice
from shutil import which

r = '\033[1;31m'
g = '\033[1;32m'
y = '\033[1;33m'
b = '\033[1;34m'
p = '\033[1;35m'
d = '\033[2;37m'
w = '\033[0m'
c = '\033[1;36m'
W = f"{w}\033[1;47m"
R = f"{w}\033[1;41m"
G = f"{w}\033[1;42m"
Y = f"{w}\033[1;43m"
B = f"{w}\033[1;44m"

home = os.getenv("HOME")
cokifile = home + "/.cookies"
space = "         "
lines = space + "-"*44
headers = {"User-Agent":"Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.334; U; id) Presto/2.5.25 Version/10.54"}
logo = f"""{b}
                          _cyqyc_
                      :>3qKKKKKKKq3>:
                  ';CpKKKKKKKKKKKKKKKpC;'
              -"iPKKKKKKKKKKKKKKKKKKKKKKKPi"-
          `~v]KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK]v~`
       ,rwKKKKKKKKKKKKKPv;,:'-':,;vPKKKKKKKKKKKKKwr,
      !KKKKKKKKKKKKKKK/             !KKKKKKKKKKKKKKK!
      !KKKKKKKKKKKKKKf               CKKKKKKKKKKKKKK!
      !KKKKKKKKKKKKKp-               -qKKKKKKKKKKKKK!
      !KKKKKKKKKKKKK>"               "\KKKKKKKKKKKKK!
      !KKKKKKKw;,_'-                   .-:,"wKKKKKKK!
      !KKKKKKKKhi*;"                   ";*ihKKKKKKKK!
      !KKKKKKKKKKKKK;                 ;KKKKKKKKKKKKK!
      !KKKKKKKKKKKKK2>'             '>2KKKKKKKKKKKKK!
      !KKKKKKKKKKKKKKKZ             ZKKKKKKKKKKKKKKK!
      !KKKKKKKKKKKKKKK5             eKKKKKKKKKKKKKKK!
      !KKKKKKKKKKKqC;-               -;CqKKKKKKKKKKK!
      <KKKKKKKKkr,                       ,rSKKKKKKKK<
       -"v]qj;-                             -;jq]v"-
                     {g}• SANTET ONLINE •
               {d}Merusak sistem tanpa menyentuh{w}
                      {c}Author by Franz{w}
                    {w}Pemalang Cyber Team{w}"""

def menu():
    os.system("clear")
    print(logo)
    print(f"""
         {W}\033[2;30m[ Pilih nomor atau ketik exit untuk keluar ]{w}

        {w}{b} 01{w} santet hp target    {d} send mallware virus
        {w}{b} 02{w} cek celah situs     {d} check vurlnerability
        {w}{b} 03{w} sadap kamera        {d} use ngrok or serveo
        {w}{b} 04{w} cek lokasi IP       {d} with IP finder
        {w}{b} 05{w} cek info device     {d} check device info
        {w}{b} 06{w} mail finder         {d} find email wih name
        {w}{b} 07{w} userrecon           {d} user reconnaissance
        {w}{b} 08{w} update program      {d} new version available
        {w}{b} 09{w} info program        {d} about this program
        """)
    mainmenu()
def mainmenu():
    while True:
        try:
            cmd = str(input(f"{space}{w}{b}>{w} Pilih Nomor:{c} "))
            if int(len(cmd)) < 6:
                if cmd in ("exit","Exit","EXIT"): exit(w+space+R+"\033[2;30m[ Keluar ]"+w)
                elif cmd in ("1","01"): santet()
                elif cmd in ("2","02"): celah()
                elif cmd in ("3","03"): sadap()
                elif cmd in ("4","04"): cekip()
                elif cmd in ("5","05"): info()
                elif cmd in ("6","06"): mailfinder()
                elif cmd in ("7","07"): userrecon()
                elif cmd in ("8","08"): update()
                elif cmd in ("9","09"): infoga()
                else: continue
            else: continue
        except KeyboardInterrupt:
            exit(f"{r}\n{space}* Aborted !")

def sadap():
   while True:
       try:
            print(f"{space}{w}Nyalakan hotspot !")
            time.sleep(0.5)
            getpass(f"\n{space}klik enter untuk melanjutkan ")
            time.sleep(0.5)
            os.system('clear')
            os.system("cd sadap ;bash saycheese.sh")
            time.sleep(2)
            menu()
       except KeyboardInterrupt:
           menu()
def update():
    print(f"{space}{w}Check update running...")
    time.sleep(4)
    print(f"{space}{w}Versi ini sudah terbaru")
    getpass(f"\n{space}klik enter untuk kembali ke menu ")
    menu()

def userrecon():
    username = str(input(f"{space}{w}{b}>{w} enter username:{c} ").lower())
    if not username: menu()
    urllist = [
        "https://facebook.com/{}",
        "https://instagram.com/{}",
        "https://twitter.com/{}",
        "https://youtube.com/{}",
        "https://vimeo.com/{}",
        "https://github.com/{}",
        "https://plus.google.com/{}",
        "https://pinterest.com/{}",
        "https://flickr.com/people/{}",
        "https://vk.com/{}",
        "https://about.me/{}",
        "https://disqus.com/{}",
        "https://bitbucket.org/{}",
        "https://flipboard.com/@{}",
        "https://medium.com/@{}",
        "https://hackerone.com/{}",
        "https://keybase.io/{}",
        "https://buzzfeed.com/{}",
        "https://slideshare.net/{}",
        "https://mixcloud.com/{}",
        "https://soundcloud.com/{}",
        "https://badoo.com/en/{}",
        "https://imgur.com/user/{}",
        "https://open.spotify.com/user/{}",
        "https://pastebin.com/u/{}",
        "https://wattpad.com/user/{}",
        "https://canva.com/{}",
        "https://codecademy.com/{}",
        "https://last.fm/user/{}",
        "https://blip.fm/{}",
        "https://dribbble.com/{}",
        "https://en.gravatar.com/{}",
        "https://foursquare.com/{}",
        "https://creativemarket.com/{}",
        "https://ello.co/{}",
        "https://cash.me/{}",
        "https://angel.co/{}",
        "https://500px.com/{}",
        "https://houzz.com/user/{}",
        "https://tripadvisor.com/members/{}",
        "https://kongregate.com/accounts/{}",
        "https://{}.blogspot.com/",
        "https://{}.tumblr.com/",
        "https://{}.wordpress.com/",
        "https://{}.devianart.com/",
        "https://{}.slack.com/",
        "https://{}.livejournal.com/",
        "https://{}.newgrounds.com/",
        "https://{}.hubpages.com",
        "https://{}.contently.com",
        "https://steamcommunity.com/id/{}",
        "https://www.wikipedia.org/wiki/User:{}",
        "https://www.freelancer.com/u/{}",
        "https://www.dailymotion.com/{}",
        "https://www.etsy.com/shop/{}",
        "https://www.scribd.com/{}",
        "https://www.patreon.com/{}",
        "https://www.behance.net/{}",
        "https://www.goodreads.com/{}",
        "https://www.gumroad.com/{}",
        "https://www.instructables.com/member/{}",
        "https://www.codementor.io/{}",
        "https://www.reverbnation.com/{}",
        "https://www.designspiration.net/{}",
        "https://www.bandcamp.com/{}",
        "https://www.colourlovers.com/love/{}",
        "https://www.ifttt.com/p/{}",
        "https://www.trakt.tv/users/{}",
        "https://www.okcupid.com/profile/{}",
        "https://www.trip.skyscanner.com/user/{}",
        "http://www.zone-h.org/archive/notifier={}",
        ]
    print(w+lines)
    for url in urllist:
        try:
            req = requests.get(url.format(username), headers=headers)
            if req.status_code == 200: color = g
            elif req.status_code == 404: color = r
            else: color = y
            print(f"  {space}{b}[{color}{req.status_code}{b}] {w}{url.format(username)}")
        except requests.exceptions.Timeout: continue
        except requests.exceptions.TooManyRedirects: break
        except requests.exceptions.ConnectionError: break
    print(w+lines)
    getpass(space+"klik enter untuk kembali ke menu ")
    menu()



def celah():
   while True:
       try:
            time.sleep(0.5)
            os.system('clear')
            os.system("cd etc/celah ;python2 scan.py")
            getpass("\n klik enter untuk kembali ke menu ")
            menu()
       except KeyboardInterrupt:
            sys.exit()

def santet():
    while True:
        try:
            time.sleep(0.5)
            ip=input(f"{space}{b}[{w}?{b}]{w} input IP target {w}:{c} ")
            if ip == "exit" :
              menu()
            if ip == "back" :
              menu()
            if len(ip) < 3 :
              print(ip)
            if len(ip) > 3 :
              time.sleep(0.1)
              print(f"{space}{w}ip target {b}[{w}{ip}{b}]{w}")
              mis=input(f"{space}{b}[{w}?{b}]{w} input port (default 4444) {w}:{c} ")
              if len(mis) < 3 :
                print(mis)
              if len(mis) > 3 :
                time.sleep(0.2)
                print(f"{space}{w}port yang digunakan {b}[{w}{mis}{b}]{w}")
                time.sleep(1)
                print(f"{space}{b}-----------------------------------")
                print(f"{space}{w}....{c}< press CTRL+C to stop >{w}....")
                print(f"{space}{b}-----------------------------------")
                time.sleep(3)

                virus = [ "trojan.zip","worm.zip","symantec.zip","cassana.zip","backdoor.tar","utf_cracker","botnet.zip","f-secure","blank404" ]

                for i in range(5):
                    while True:
                        data = choice(virus)
                        print(f"{space}{w}sending {r}{data}{w} to ip{g} {ip}{w} with port{g} {mis}{w}")
                        time.sleep(1)
        except KeyboardInterrupt:
            print(menu)

def mailfinder():
    fullname = str(input(f"{space}{b}>{w} masukkan nama:{c} ").lower())
    if not fullname: menu()
    print(w+lines)
    data = [
        "gmail.com",
        "yahoo.com",
        "hotmail.com",
        "aol.com",
        "msn.com",
        "comcast.net",
        "live.com",
        "rediffmail.com",
        "ymail.com",
        "outlook.com",
        "cox.net",
        "googlemail.com",
        "rocketmail.com",
        "att.net",
        "facebook.com",
        "bellsouth.net",
        "charter.net",
        "sky.com",
        "earthlink.net",
        "optonline.net",
        "qq.com",
        "me.com",
        "gmx.net",
        "mail.com",
        "ntlworld.com",
        "frontiernet.net",
        "windstream.net",
        "mac.com",
        "centurytel.net",
        "aim.com",
        ]
    listuser = [
        fullname.replace(" ",""),
        fullname.replace(" ","")+"123",
        fullname.replace(" ","")+"1234",
        ]
    for name in fullname.split(" "):
        listuser.append(name)
        listuser.append(name+"123")
        listuser.append(name+"1234")
    f = open("result_mailfinder.txt","w")
    ok = []
    try:
        for user in listuser:
            for domain in data:
                email = user + "@" + domain
                api = "0c6ad1fd-f753-4628-8c0a-7968e722c6c7"
                response = requests.get(
                    "https://isitarealemail.com/api/email/validate",
                    params = {'email': email},
                    headers = {'Authorization': "Bearer " + api })
                status = response.json()['status']
                if status == "valid":
                    ok.append(email)
                    f.write(email+"\n")
                    print(f"{space}{B} DONE {w} Status: {g}valid{w} Email: {email}")
                else: pass
    except KeyboardInterrupt:
        print("\r"),;sys.stdout.flush()
        pass
    f.close()
    print(w+lines)
    print(f"{space}{b}>{w} {str(len(ok))} retrieved as: {y}result_mailfinder.txt{w}")
    getpass(space+"klik enter untuk kembali ke menu ")
    menu()

def info():

    import platform

    my_system = platform.uname()
    time.sleep(0.1)
    print(f"\n{space}{b}System:{w} {my_system.system}")
    time.sleep(0.1)
    print(f"{space}{b}Node Name:{w} {my_system.node}")
    time.sleep(0.1)
    print(f"{space}{b}Release:{w} {my_system.release}")
    time.sleep(0.1)
    print(f"{space}{b}Version:{w} {my_system.version}")
    time.sleep(0.1)
    print(f"{space}{b}Machine:{w} {my_system.machine}")
    time.sleep(0.1)
    print(f"{space}{b}Processor:{w} {my_system.processor}\n")
    getpass(space+"klik enter untuk kembali ke menu ")
    menu()

def cekip():
    print(f"{space}{g}>{w} local IP: {os.popen('curl ifconfig.co --silent').readline().strip()}")
    x = str(input(f"{space}{g}>{w} enter IP:{c} "))
    if x.split(".")[0].isnumeric(): pass
    else: menu()
    print(w+lines)
    req = requests.get("https://ipinfo.io/"+x+"/json").json()
    try: ip = "IP: "+req["ip"]
    except KeyError: ip = ""
    try: city = "CITY: "+req["city"]
    except KeyError: city = ""
    try: country = "COUNTRY: "+req["country"]
    except KeyError: country = ""
    try: loc = "LOC: "+req["loc"]
    except KeyError: loc = ""
    try: org = "ORG: "+req["org"]
    except KeyError: org = ""
    try: tz = "TIMEZONE: "+req["timezone"]
    except KeyError: tz = ""
    z = [ip, city, country, loc, org, tz]
    for res in z:
        print(f"{space}{g}-{w} {res}")
    print(w+lines)
    getpass(space+"klik enter untuk kembali ke menu ")
    menu()

def infoga():
    os.system('clear')
    os.system('cat info.txt')
    getpass(w+'[ klik enter untuk kembali ke menu ]')
    menu()

menu()
mainmenu()


