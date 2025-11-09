print("Chan Remastered")
import requests

data = requests.get(
    url = "https://api.hypixel.net/player",
    params = {
        "key": "KEY",
        "name": "overambitious"
    }
).json()

# 1. Type .\.venv\Scripts\Activate.ps1      to activate venv 
# 2. pyinstaller --onefile --name ChanRemastered main.py     to update the exe

online = "ONLINE:"


def main():

    names = splitnames(find_latest_line())
    print(names)
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