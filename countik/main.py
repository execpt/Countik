import requests
import json
import os
from vardxg import Center, Colors
import time

os.system('cls')

def banner():
    vardxg = ("""
████████╗██╗██╗  ██╗ ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗
╚══██╔══╝██║██║ ██╔╝██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝
   ██║   ██║█████╔╝ ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║   
   ██║   ██║██╔═██╗ ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║   
   ██║   ██║██║  ██╗╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║   
   ╚═╝   ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   
    """)
    print(Center.XCenter(vardxg))


class checktiktok:
    def __init__(self) -> None:
        pass

    banner()

    link = input("\n [?] Enter Video ID >>> ")

    if link == (link):
        os.system('cls')
        url = "https://countik.com/api/videoinfo/" + link
        payload = ""
        response = requests.request("GET", url, data=payload)
        data = json.loads(response.text)
        status = data['status']
        creator = data['creator']
        ide = data['id']
        descr = data['desc']
        create_date = data['create_date']
        cover = data['cover']
        likes = data['likes']
        views = data['plays']
        shares = data['shares']
        comments = data['comments']

        while True:
            for _ in range(2):
                os.system('cls')
                print("\n Status => ", status, Colors.green)
                print("\n Creator => ", creator, Colors.green)
                print("\n Video ID => ", ide, Colors.green)
                print("\n Description => ", descr, Colors.green)
                print("\n Creation Date => ", create_date, Colors.green)
                print("\n Cover => ", cover, Colors.green)
                print("\n Likes => ", likes, Colors.green)
                print("\n Views => ", views, Colors.green)
                print("\n Shares => ", shares,  Colors.green)
                print("\n Comments => ", comments, Colors.green)
                time.sleep(2)
                os.system('cls')
    else:
        exit

# => Made by @vardxg on Telegram!