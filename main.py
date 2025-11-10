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

    players = {}
    counter = 0
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
        counter += 1
        url = f"https://api.hypixel.net/player?key={API_KEY}&name={name}"
        data = getInfo(url)
        finals = str(data["player"]["stats"]["Bedwars"]["final_kills_bedwars"])
        wins = str(data["player"]["stats"]["Bedwars"]["wins_bedwars"])
        kills = str(data["player"]["stats"]["Bedwars"]["kills_bedwars"])
        bedsbroken = str(data["player"]["stats"]["Bedwars"]["beds_broken_bedwars"])
        
        player = "player" + str(counter)
        players[player] = {
            "name": name,
            "finals": finals,
            "wins": wins,
            "kills": kills,
            "bedsbroken": bedsbroken
        }
        pprint(players)

        print(players[player]['kills'])



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
    try:
        main()
    except Exception as e:
        print(f"\nError occurred: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...")