import requests
import json
from pprint import pprint


def getInfo(call):
    r = requests.get(call)
    return r.json()

API_FILE = open("C:/Users/ethan/OneDrive/Desktop/api_key.txt", "r")
API_KEY = API_FILE.read().strip()


# 1. .\.venv\Scripts\Activate.ps1      to activate venv 
# 2. pyinstaller --onefile --name ChanRemastered main.py     to update the exe

online = "ONLINE:"

def main():
    

    names = splitnames(find_latest_line())

    NAME_W = 20
    FIN_W = 12
    WINS_W = 8
    KILLS_W = 8
    BEDS_W = 12

    header = f"{'name':<{NAME_W}}{'finals':>{FIN_W}}{'wins':>{WINS_W}}{'kills':>{KILLS_W}}{'beds':>{BEDS_W}}"
    print(header)
    print('-' * len(header))
    
    for name in names:
        url = f"https://api.hypixel.net/player?key={API_KEY}&name={name}"
        data = getInfo(url)

        finals = str(data["player"]["stats"]["Bedwars"]["final_kills_bedwars"])
        wins = str(data["player"]["stats"]["Bedwars"]["wins_bedwars"])
        kills = str(data["player"]["stats"]["Bedwars"]["kills_bedwars"])
        bedsbroken = str(data["player"]["stats"]["Bedwars"]["beds_broken_bedwars"])
        
        print(f"{name:<{NAME_W}}{finals:>{FIN_W}}{wins:>{WINS_W}}{kills:>{KILLS_W}}{bedsbroken:>{BEDS_W}}")


    
    input("Press Enter to exit...")
    

def find_latest_line():
    file = open('C:/Users/ethan/AppData/Roaming/.minecraft/logs/blclient/minecraft/latest.log', 'r')
    for line in reversed(file.readlines()):
        if online in line:
            print(line)
            return line 
    else:
        print("No entries found")



def splitnames(line):

    index = line.find(online)
    line = line[index + len(online):]
    names = line.strip().split(", ")
    return names



if __name__ == "__main__":
    main()